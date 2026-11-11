"""Verifica a reprodutibilidade da amostra A01 a partir da base entregue.
Execução: python verificar_amostra_A01.py BASE.csv.gz AMOSTRA.csv
Requer pandas. Não regenera a população de 500.000 registros.
"""
import sys
from pathlib import Path
import pandas as pd

if len(sys.argv) != 3:
    raise SystemExit('Uso: python verificar_amostra_A01.py BASE.csv.gz AMOSTRA.csv')
base_path, amostra_path = map(Path, sys.argv[1:])
base = pd.read_csv(base_path)
original = pd.read_csv(amostra_path)
reproduzida = base.sample(n=600, random_state=241003419)
colunas_iguais = list(original.columns) == list(reproduzida.columns)
ids_iguais = original['registro_id'].tolist() == reproduzida['registro_id'].tolist()
conteudo_igual = colunas_iguais and original.reset_index(drop=True).equals(reproduzida.reset_index(drop=True))
print('Base:', base_path, '| registros:', len(base))
print('Amostra:', amostra_path, '| registros:', len(original))
print('Semente: 241003419')
print('Colunas iguais:', colunas_iguais)
print('Identificadores na mesma ordem:', ids_iguais)
print('Conteúdo integral igual:', conteudo_igual)
if not conteudo_igual:
    raise SystemExit('FALHA: a amostra não coincide integralmente.')
print('SUCESSO: seleção reproduzida a partir da base entregue.')
