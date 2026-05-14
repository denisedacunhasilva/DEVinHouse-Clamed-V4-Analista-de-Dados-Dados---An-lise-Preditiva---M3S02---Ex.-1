# M3S03 - Ex03

## Objetivo

Utilizar validacao cruzada (`cross_val_score`) no modelo de regressao linear e
responder se o resultado e consistente com o teste simples.

## Base de referencia

O projeto usa a mesma base local:

`data/raw/dados_AP.csv`

Referencia informada no card:

- [Base no Google Drive](https://drive.google.com/file/d/137zf2K5lqh_FAdVKkHiHFPQ6KOJ7gtNq/view?usp=drive_link)

## Arquivo principal

- [cross_validation_regressao_linear.py](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s03/ex03/cross_validation_regressao_linear.py)

## Como executar

```powershell
python exercicios/m3s03/ex03/cross_validation_regressao_linear.py
```

## Resultados da validacao cruzada

Foi utilizada validacao cruzada com `5` folds no modelo de Regressao Linear,
com `shuffle=True` e `random_state=42`.

### R2

- folds: `0.9544`, `0.9547`, `0.9557`, `0.9565`, `0.9546`
- media: `0.9552`
- desvio padrao: `0.0008`

### MAE

- folds: `18.7022`, `18.5646`, `18.7125`, `18.4525`, `18.6456`
- media: `18.6155`
- desvio padrao: `0.0969`

### RMSE

- folds: `28.0073`, `28.0779`, `27.9376`, `27.5494`, `28.0093`
- media: `27.9163`
- desvio padrao: `0.1887`

## Comparacao com o teste simples

No teste simples da Regressao Linear, os resultados tinham sido:

- `MAE = 18.7022`
- `RMSE = 28.0073`
- `R2 = 0.9544`

## Resposta

### O resultado e consistente com o teste simples?

Sim. O resultado da validacao cruzada e **consistente** com o teste simples.

As medias da validacao cruzada ficaram muito proximas das metricas obtidas no
teste simples:

- `R2` ficou em `0.9552` na validacao cruzada contra `0.9544` no teste simples
- `MAE` ficou em `18.6155` contra `18.7022`
- `RMSE` ficou em `27.9163` contra `28.0073`

Alem disso, os desvios padrao foram baixos, o que sugere que o desempenho do
modelo linear se manteve estavel entre as diferentes divisoes da base. Isso
reforca a ideia de que a regressao linear apresenta comportamento consistente
e confiavel nesta base.
