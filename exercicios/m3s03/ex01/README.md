# M3S03 - Ex01

## Objetivo

Treinar um segundo modelo utilizando `DecisionTreeRegressor`.

## Base de referencia

O projeto usa a mesma base local:

`data/raw/dados_AP.csv`

Referencia informada no card:

- [Base no Google Drive](https://drive.google.com/file/d/137zf2K5lqh_FAdVKkHiHFPQ6KOJ7gtNq/view?usp=drive_link)

## Arquivo principal

- [decision_tree_regressor.py](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s03/ex01/decision_tree_regressor.py)

## Como executar

```powershell
python exercicios/m3s03/ex01/decision_tree_regressor.py
```

## O que o script faz

- carrega a base
- separa `X` e `y`
- divide os dados em 80% treino e 20% teste
- treina um `DecisionTreeRegressor`
- gera previsoes no conjunto de teste

## Resultado obtido na base atual

- modelo treinado com sucesso
- profundidade da arvore: `32`
- numero de folhas: `15110`
- `MAE = 11.7173`
- `RMSE = 14.7410`
- `R2 = 0.9874`
