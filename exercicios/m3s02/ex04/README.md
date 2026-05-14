# M3S02 - Ex04

## Objetivo

Responder, com base nas metricas calculadas no `M3S02 - Ex03`:

- O modelo apresenta bom desempenho?
- Qual metrica e mais relevante nesse caso?

## Base de referencia

O exercicio usa a mesma base do projeto, armazenada localmente em:

`data/raw/dados_AP.csv`

Referencia informada no card:

- [Base no Google Drive](https://drive.google.com/file/d/137zf2K5lqh_FAdVKkHiHFPQ6KOJ7gtNq/view?usp=drive_link)

## Metricas consideradas

Com base no `M3S02 - Ex03`:

- `MAE = 18.7022`
- `RMSE = 28.0073`
- `R2 = 0.9544`

## Respostas

### O modelo apresenta bom desempenho?

Sim. O modelo apresenta **bom desempenho** nesta base.

O principal sinal disso e o `R2 = 0.9544`, que indica que o modelo consegue
explicar cerca de 95% da variacao da demanda no conjunto de teste. Alem disso,
o `MAE = 18.7022` mostra que, em media, a previsao erra aproximadamente 19
unidades de demanda, o que e um valor relativamente baixo para esta base.

### Qual metrica e mais relevante nesse caso?

A metrica mais relevante neste caso e o **MAE**.

Isso acontece porque o `MAE` mostra diretamente, em unidades da variavel
`demanda`, qual e o erro medio do modelo. No contexto de negocio, essa leitura
e mais intuitiva para apoiar decisoes como planejamento de estoque e reposicao.

O `RMSE` tambem e util por penalizar mais os erros grandes, e o `R2` ajuda a
avaliar o ajuste geral do modelo. Ainda assim, para interpretacao pratica no
dia a dia, o `MAE` tende a ser o indicador mais facil de comunicar.
