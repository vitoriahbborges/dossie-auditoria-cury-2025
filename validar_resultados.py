import pandas as pd
from pathlib import Path
p=Path(__file__).resolve().parent
df=pd.read_csv(p/'dados/base_500000_contas_receber_SINTETICA.csv.gz')
r=pd.read_csv(p/'resultados/resumo.csv')
g=pd.read_csv(p/'resultados/gabarito_erros_SINTETICOS.csv')
a=pd.read_csv(p/'resultados/amostra_600_SINTETICA.csv')
assert len(df)==500000 and df.registro_id.nunique()==500000
assert len(g)==501 and len(a)==600
assert (df.saldo_bruto_centavos.sum()-df.pecld_centavos.sum()-df.distratos_centavos.sum()-df.avp_centavos.sum())/100==2157943000
print(r.to_string(index=False)); print('Validação independente concluída.')
