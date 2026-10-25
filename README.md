# Auditoria 1 — CURY — Vitória Helena Bastos Borges

Data documental: **24/10/2026**. Matrícula 241003419.

## Conteúdo
- `DOSSIE_COMPLETO_CURY_VITORIA_24-10-2026.pdf`: relatório estruturado inspirado na organização do exemplo apresentado e 27 papéis de trabalho anexados.
- `DFP_CURY_2025_FONTE.pdf`: demonstrações públicas fornecidas pela estudante.
- `dados/`: base sintética de 500.000 registros.
- `resultados/`: resumo, amostra, matriz e gabarito de erros artificiais.
- `validar_resultados.py`: conferência independente dos arquivos de resultados, sem reconstituir a geração original.

## Método e limites
A base sintética foi calibrada para o saldo líquido de clientes de R$ 2.157.943.000. Não é razão auxiliar real da Cury. Os 501 achados são erros artificiais. Circularizações, inspeções e testes internos não foram executados.

A matriz analítica possui coluna `saldo_bruto_centavos`, mas os valores agregados estão em **reais**. Não alterar unidade automaticamente.

O script original de geração usado no Colab não consta dos arquivos enviados. Para reprodutibilidade integral, adicionar esse script ou notebook ao repositório.

A data documental foi ajustada por solicitação da estudante, não sendo uma certificação de quando os arquivos foram gerados.

## Download da base completa
https://docs.google.com/spreadsheets/d/1wbxUMKsK55tXEy-0NM6TtlNkCi8Kbc7rwL0FdouDxwY/edit?usp=sharing
