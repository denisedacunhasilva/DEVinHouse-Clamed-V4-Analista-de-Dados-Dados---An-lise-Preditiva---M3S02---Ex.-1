# M3S02 - Ex04

## Objetivo

Responder, com base nas métricas calculadas no `M3S02 - Ex03`:

- O modelo apresenta bom desempenho?
- Qual métrica é mais relevante nesse caso?

## Base de referência

O exercício usa a mesma base do projeto, armazenada localmente em:

`data/raw/dados_AP.csv`

Referência informada no card:

- [Base no Google Drive](https://drive.google.com/file/d/137zf2K5lqh_FAdVKkHiHFPQ6KOJ7gtNq/view?usp=drive_link)

## Métricas consideradas

Com base no `M3S02 - Ex03`:

- `MAE = 18.7022`
- `RMSE = 28.0073`
- `R2 = 0.9544`

## Respostas

### O modelo apresenta bom desempenho?

Sim. O modelo apresenta **bom desempenho** nesta base.

O principal sinal disso é o `R2 = 0.9544`, que indica que o modelo consegue
explicar cerca de 95% da variação da demanda no conjunto de teste. Além disso,
o `MAE = 18.7022` mostra que, em média, a previsão erra aproximadamente 19
unidades de demanda, o que é um valor relativamente baixo para esta base.

### Qual métrica é mais relevante nesse caso?

A métrica mais relevante neste caso é o **MAE**.

Isso acontece porque o `MAE` mostra diretamente, em unidades da variável
`demanda`, qual é o erro médio do modelo. No contexto de negócio, essa leitura
é mais intuitiva para apoiar decisões como planejamento de estoque e reposição.

O `RMSE` também é útil por penalizar mais os erros grandes, e o `R2` ajuda a
avaliar o ajuste geral do modelo. Ainda assim, para interpretação prática no
dia a dia, o `MAE` tende a ser o indicador mais fácil de comunicar.
