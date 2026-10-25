"""Cury 2025 — estudo didático, registros 100% sintéticos.
Colab: %run /content/gerar_analisar_colab.py (opcionalmente enviar PDF ao ambiente).
"""
from pathlib import Path
import numpy as np, pandas as pd
from scipy.stats import chi2_contingency
ROOT=Path('/content/cury_recebiveis_241003419') if Path('/content').exists() else Path(__file__).resolve().parents[1]
for d in ['dados','resultados']: (ROOT/d).mkdir(parents=True,exist_ok=True)
SEED=241003419; rng=np.random.default_rng(SEED); N=500_000
# Valores divulgados em R$ mil, Nota 5, pp. 101-102 do PDF (não são microdados).
GROSS={'unidades_concluidas':258_102_000,'unidades_em_construcao':2_130_268_000,'titulos_spe':68_663_000}
DEDUCTIONS={'pecld':188_499_000,'distratos':51_812_000,'avp':58_779_000}
AGE={'a_vencer_1_360':446_345_000,'a_vencer_361_720':705_133_000,'a_vencer_721_mais':1_166_595_000,'vencido_1_30':21_363_000,'vencido_31_90':11_980_000,'vencido_91_mais':105_617_000}
# Nota 5: cronograma inclui títulos SPE; a combinação exata categoria x vencimento não é divulgada.
assert sum(GROSS.values())==sum(AGE.values())==2_457_033_000
assert sum(GROSS.values())-sum(DEDUCTIONS.values())==2_157_943_000

def split_exact(total,weights):
    w=np.asarray(weights,dtype=np.float64); w=w/w.sum(); cents=int(total)*100
    raw=w*cents; v=np.floor(raw).astype(np.int64); rest=cents-int(v.sum())
    if rest: v[np.argsort(raw-v)[-rest:]]+=1
    assert int(v.sum())==cents
    return v

def assign_groups(totals, counts):
    groups=[]; values=[]
    for key,total in totals.items():
        n=counts[key]; groups.extend([key]*n); values.append(split_exact(total,rng.lognormal(0,0.85,n)))
    return np.array(groups),np.concatenate(values)

cat_counts={'unidades_concluidas':55_000,'unidades_em_construcao':430_000,'titulos_spe':15_000}
cat,gross=assign_groups(GROSS,cat_counts)
perm=rng.permutation(N); cat=cat[perm]; gross=gross[perm]
df=pd.DataFrame({'registro_id':np.arange(1,N+1,dtype=np.int64),'natureza_credito':cat,'saldo_bruto_centavos':gross})
# Estratificação de vencimento respeita montantes públicos, sem alegar cruzamento real.
age_counts={'a_vencer_1_360':90_000,'a_vencer_361_720':145_000,'a_vencer_721_mais':210_000,'vencido_1_30':10_000,'vencido_31_90':10_000,'vencido_91_mais':35_000}
age,age_values=assign_groups(AGE,age_counts)
# Saldo por aging é um segundo rateio sintético; evitar fingir que ambos são a mesma matriz observada.
# Para conciliar as DUAS margens, construir matriz sintética via ajuste iterativo (IPF) em centavos.
cat_names=list(GROSS); age_names=list(AGE)
rows=np.array([cat_names.index(x) for x in cat]); cols=np.array([age_names.index(x) for x in age]);
# Primeiro alocar os registros aos buckets, preservando quantidades, depois escalar margens iterativamente.
age=age[rng.permutation(N)]; cols=np.array([age_names.index(x) for x in age]);
w=rng.lognormal(0,.8,N)
for _ in range(55):
    s=np.bincount(rows,weights=w,minlength=3); w*=np.array(list(GROSS.values()))[rows]/s[rows]
    s=np.bincount(cols,weights=w,minlength=6); w*=np.array(list(AGE.values()))[cols]/s[cols]
# arredondamento exato de ambas as margens: transporte de resíduos entre células
mat=np.zeros((3,6),dtype=np.int64)
for i in range(3):
 for j in range(6):
  ix=np.flatnonzero((rows==i)&(cols==j)); mat[i,j]=len(ix)
# Em vez de IPF sobre microdados, usar pesos já convergidos e ajustar centavos dentro de grupos.
vals=np.rint(w*100).astype(np.int64)
row_target=np.array(list(GROSS.values()),dtype=np.int64)*100
col_target=np.array(list(AGE.values()),dtype=np.int64)*100
# Correção em centavos via células (i,j), cada célula possui registros.
cell_idx={(i,j):np.flatnonzero((rows==i)&(cols==j)) for i in range(3) for j in range(6)}
# Ajuste linhas primeiro, na maior posição da célula.
for i in range(3):
 ix=np.flatnonzero(rows==i); delta=int(row_target[i]-vals[ix].sum()); vals[ix[0]]+=delta
# Ajustar colunas transferindo valores entre registros da mesma linha (mantém margens das linhas).
for j in range(5):
 delta=int(col_target[j]-vals[cols==j].sum())
 for i in range(3):
  ix1=cell_idx[i,j]; ix2=cell_idx[i,5]
  if len(ix1) and len(ix2):
   if delta>0:
    # retirar de célula final sem negativar valores; grande capacidade nos 3 grupos
    pool=ix2[np.argsort(vals[ix2])[::-1]]
    for donor in pool:
     take=min(delta,max(0,int(vals[donor])-1))
     if take: vals[donor]-=take; vals[ix1[0]]+=take; delta-=take
     if delta==0: break
   elif delta<0:
    pool=ix1[np.argsort(vals[ix1])[::-1]]
    for donor in pool:
     take=min(-delta,max(0,int(vals[donor])-1))
     if take: vals[donor]-=take; vals[ix2[0]]+=take; delta+=take
     if delta==0: break
  if delta==0:break
 if delta!=0: raise RuntimeError(f'Falha ao conciliar aging: {j}: {delta}')
assert (vals>0).all()
assert np.array_equal(np.bincount(rows,weights=vals).astype(np.int64),row_target)
assert np.array_equal(np.bincount(cols,weights=vals).astype(np.int64),col_target)
df['saldo_bruto_centavos']=vals; df['faixa_vencimento']=age
# Deduções são ajustes contábeis alocados sinteticamente, não necessariamente lançamentos contratuais reais.
for name,total in DEDUCTIONS.items():
 eligible=np.flatnonzero(df.natureza_credito.ne('titulos_spe').to_numpy()) if name!='pecld' else np.arange(N)
 allocated=split_exact(total,rng.lognormal(0,.8,len(eligible)))
 a=np.zeros(N,dtype=np.int64); a[eligible]=allocated; df[name+'_centavos']=a
# Ajustes não são aplicados ao saldo bruto por linha como se fossem comprovadamente associados ao contrato.
df['saldo_liquido_centavos']=df['saldo_bruto_centavos']-df[[x+'_centavos' for x in DEDUCTIONS]].sum(axis=1)
df['empreendimento_sintetico']='EMP-'+pd.Series(rng.integers(1,601,N)).astype(str).str.zfill(4)
df['regiao_sintetica']=rng.choice(['SP','RJ','Outra'],N,p=[.58,.39,.03])
df['tipo_unidade_sintetico']=rng.choice(['Apartamento','Unidade comercial','Outro'],N,p=[.95,.03,.02])
df['mes_referencia_sintetico']=rng.integers(1,13,N)
df['origem']='SINTETICO_NAO_CORRESPONDE_A_CONTRATOS_REAIS'
# Erros artificiais, em campo separado, preservando a conciliação da coluna base.
err_idx=rng.choice(N,501,replace=False)
df['valor_teste_centavos']=df.saldo_bruto_centavos.copy()
df.loc[err_idx,'valor_teste_centavos']+=rng.integers(10000,1000000,len(err_idx))
gabarito=df.loc[err_idx,['registro_id','saldo_bruto_centavos','valor_teste_centavos']].copy()
gabarito['diferenca_centavos']=gabarito.valor_teste_centavos-gabarito.saldo_bruto_centavos
exceptions=df.loc[df.valor_teste_centavos.ne(df.saldo_bruto_centavos)]
sample=df.sample(n=600,random_state=SEED)
summary=pd.DataFrame([
 ['registros',len(df)],['ids_unicos',df.registro_id.nunique()],['saldo_bruto_reais',df.saldo_bruto_centavos.sum()/100],
 ['deducoes_reais',df[[x+'_centavos' for x in DEDUCTIONS]].to_numpy().sum()/100],['saldo_liquido_reais',df.saldo_liquido_centavos.sum()/100],
 ['excecoes_inseridas',len(gabarito)],['excecoes_detectadas_censo',len(exceptions)],['excecoes_amostra_600',int(sample.valor_teste_centavos.ne(sample.saldo_bruto_centavos).sum())]],columns=['metrica','valor'])
df.to_csv(ROOT/'dados/base_500000_contas_receber_SINTETICA.csv.gz',index=False,compression='gzip')
gabarito.to_csv(ROOT/'resultados/gabarito_erros_SINTETICOS.csv',index=False)
sample.to_csv(ROOT/'resultados/amostra_600_SINTETICA.csv',index=False)
summary.to_csv(ROOT/'resultados/resumo.csv',index=False)
(df.groupby(['natureza_credito','faixa_vencimento'],observed=True).saldo_bruto_centavos.sum()/100).to_csv(ROOT/'resultados/matriz_analitica_SINTETICA.csv')
print(summary.to_string(index=False));print('Arquivos em',ROOT)
