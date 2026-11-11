# # Dossiê Acadêmico de Auditoria — Cury Construtora e Incorporadora S.A. (2025)

**Universidade de Brasília — Auditoria 1 (CCA0024)**

**Discente:** Vitória Helena Bastos Borges  
**Matrícula:** 241003419  
**Data do trabalho original:** 24/10/2026  
**Revisão documental complementar:** 11/11/2026

## 1. Apresentação

Este repositório reúne os documentos e resultados de um estudo acadêmico de auditoria contábil sobre as demonstrações financeiras consolidadas da Cury Construtora e Incorporadora S.A., referentes ao exercício de 2025, com dados comparativos de 2024.

O estudo concentra-se na análise de contas a receber, utilizando demonstrações financeiras públicas, uma base sintética de 500.000 registros e procedimentos automatizados desenvolvidos em Python.

## 2. Organização dos arquivos

| Pasta ou arquivo | Conteúdo |
|---|---|
| `DOSSIÊ DE AUDITORIA/` | Dossiê acadêmico com metodologia, análises e conclusões |
| `PAPÉIS DE TRABALHO/` | 27 papéis de trabalho fundamentados nas normas de auditoria |
| `RELATÓRIO DE AUDITORIA/` | Relatório acadêmico e conclusões do estudo |
| `DEMONSTRAÇÕES B3/` | Demonstrações Financeiras Padronizadas da Cury referentes a 2025 |
| `BASE SIMULADA/` | Base sintética de 500.000 registros, em formato CSV compactado |
| `CÓDIGO/` | Código de geração, análise e verificação da amostra |
| `resultados/` | Arquivos de resultados, amostragem, testes e memórias de cálculo |
| `validar_resultados.py` | Script de validação dos arquivos de resultados |

## 3. Base sintética e resultados

A base sintética foi construída para demonstrar procedimentos computacionais de auditoria, sem utilizar registros reais de clientes da companhia.

| Indicador | Resultado |
|---|---:|
| Registros sintéticos | 500.000 |
| Identificadores únicos | 500.000 |
| Saldo bruto simulado | R$ 2.457.033.000,00 |
| Deduções simuladas | R$ 299.090.000,00 |
| Saldo líquido simulado | R$ 2.157.943.000,00 |
| Exceções artificiais identificadas na população | 501 |
| Registros selecionados na amostra | 600 |
| Exceções identificadas na amostra | 0 |

O saldo líquido foi calibrado para corresponder ao total consolidado de contas a receber divulgado nas demonstrações financeiras de 2025.

A ausência de exceções na amostra de 600 registros não significa inexistência de erros na população.

## 4. Código e reprodutibilidade

O repositório disponibiliza os seguintes códigos:

- `CÓDIGO/gerar_analisar_colab.py`: geração e análise da base sintética.
- `CÓDIGO/verificar_amostra_A01.py`: verificação da reprodutibilidade da seleção amostral.
- `validar_resultados.py`: conferência dos resultados gerados.

A seleção da amostra utiliza a semente aleatória `241003419`.

A verificação complementar da amostra está documentada em `resultados/resultado_verificacao_A01.txt`.

A reprodução da seleção amostral a partir da base entregue não equivale, por si só, à regeneração integral da população sintética.

## 5. Memórias de cálculo e procedimentos complementares

Foram incorporados os seguintes documentos:

**PT 530 — Amostragem:** documentação do algoritmo de seleção e da verificação dos 600 registros.

**PT 540 — Estimativas contábeis:** arquivo `resultados/memoria_calculo_PT540.xlsx`, com fórmulas editáveis e três cenários de sensibilidade das deduções sintéticas.

**PT 560 — Eventos subsequentes:** arquivo `resultados/pesquisa_eventos_subsequentes_PT560.xlsx`, contendo eventos identificados, datas, fontes documentais, classificações preliminares e limitações da pesquisa.

## 6. Limitações metodológicas

Este trabalho possui finalidade exclusivamente acadêmica e não constitui auditoria independente ou emissão de opinião profissional sobre as demonstrações financeiras da Cury.

Os 501 achados são exceções artificiais introduzidas na simulação. Não representam irregularidades constatadas na companhia.

Não foram executadas circularizações de clientes, inspeções de documentos internos ou testes de controles reais.

A análise de sensibilidade de ±10% das deduções não representa recálculo independente da PECLD, do ajuste a valor presente (AVP) ou do reconhecimento de receitas pelo percentual de conclusão (PoC).

A matriz analítica original contém a coluna `saldo_bruto_centavos`, embora seus valores agregados estejam expressos em reais. Essa particularidade deve ser considerada na interpretação dos resultados.

## 7. Download da base completa

A base sintética completa pode ser consultada no link:

[**Acessar base simulada de 500.000 registros — Google Sheets**](https://docs.google.com/spreadsheets/d/1wbxUMKsK55tXEy-0NM6TtINkCi8Kbc7rwL0FdouDxwY/edit?usp=sharing)

O arquivo compactado também está disponibilizado na pasta `BASE SIMULADA/` do repositório.

## 8. Referências normativas

BRASIL. Conselho Federal de Contabilidade. Normas Brasileiras de Contabilidade aplicadas à auditoria independente, especialmente NBC TA 230, NBC TA 500, NBC TA 530, NBC TA 540 e NBC TA 560.

COMITÊ DE PRONUNCIAMENTOS CONTÁBEIS. CPC 24 — Evento Subsequente.

## 9. Histórico de revisão

**24/10/2026:** versão documental original do estudo.

**11/11/2026:** revisão complementar dos papéis de trabalho, atualização da documentação de reprodutibilidade da amostra, inclusão da memória de cálculo do PT 540 e da matriz de eventos subsequentes do PT 560.
