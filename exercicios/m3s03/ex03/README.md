# M3S03 - Ex03

## Objetivo

Utilizar validação cruzada (`cross_val_score`) no modelo de regressão linear e
responder se o resultado é consistente com o teste simples.

## Base de referência

O projeto usa a mesma base local:

`data/raw/dados_AP.csv`

Referência informada no card:

- [Base no Google Drive](https://drive.google.com/file/d/137zf2K5lqh_FAdVKkHiHFPQ6KOJ7gtNq/view?usp=drive_link)

## Arquivo principal

- [cross_validation_regressao_linear.py](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s03/ex03/cross_validation_regressao_linear.py)

## Como executar

```powershell
python exercicios/m3s03/ex03/cross_validation_regressao_linear.py
```

## Resultados da validação cruzada

Foi utilizada validação cruzada com `5` folds no modelo de Regressão Linear,
com `shuffle=True` e `random_state=42`.

### R2

- folds: `0.9544`, `0.9547`, `0.9557`, `0.9565`, `0.9546`
- média: `0.9552`
- desvio padrão: `0.0008`

### MAE

- folds: `18.7022`, `18.5646`, `18.7125`, `18.4525`, `18.6456`
- média: `18.6155`
- desvio padrão: `0.0969`

### RMSE

- folds: `28.0073`, `28.0779`, `27.9376`, `27.5494`, `28.0093`
- média: `27.9163`
- desvio padrão: `0.1887`

## Comparação com o teste simples

No teste simples da Regressão Linear, os resultados tinham sido:

- `MAE = 18.7022`
- `RMSE = 28.0073`
- `R2 = 0.9544`

## Resposta

### O resultado é consistente com o teste simples?

Sim. O resultado da validação cruzada é **consistente** com o teste simples.

As médias da validação cruzada ficaram muito próximas das métricas obtidas no
teste simples:

- `R2` ficou em `0.9552` na validação cruzada contra `0.9544` no teste simples
- `MAE` ficou em `18.6155` contra `18.7022`
- `RMSE` ficou em `27.9163` contra `28.0073`

Além disso, os desvios padrão foram baixos, o que sugere que o desempenho do
modelo linear se manteve estável entre as diferentes divisões da base. Isso
reforça a ideia de que a regressão linear apresenta comportamento consistente
e confiável nesta base.
