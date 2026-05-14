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

Foi utilizada validacao cruzada com `5` folds no modelo de Regressao Linear.

### R2

- folds: `0.9595`, `0.9514`, `0.9544`, `0.9547`, `0.9557`
- media: `0.9551`
- desvio padrao: `0.0026`

### MAE

- folds: `18.1458`, `18.7719`, `19.0288`, `18.5722`, `18.5690`
- media: `18.6175`
- desvio padrao: `0.2898`

### RMSE

- folds: `26.7472`, `28.6569`, `28.3443`, `27.9656`, `27.8608`
- media: `27.9149`
- desvio padrao: `0.6487`

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

- `R2` ficou em `0.9551` na validacao cruzada contra `0.9544` no teste simples
- `MAE` ficou em `18.6175` contra `18.7022`
- `RMSE` ficou em `27.9149` contra `28.0073`

Alem disso, os desvios padrao foram baixos, o que sugere que o desempenho do
modelo linear se manteve estavel entre as diferentes divisoes da base. Isso
reforca a ideia de que a regressao linear apresenta comportamento consistente
e confiavel nesta base.
