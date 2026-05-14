# M3S03 - Ex02

## Objetivo

Comparar os modelos **Regressao Linear** e **Arvore de Decisao** e responder:

- Qual teve melhor desempenho?
- Qual parece mais confiavel para negocio?

## Base de referencia

O projeto usa a mesma base local:

`data/raw/dados_AP.csv`

## Arquivo principal

- [comparar_modelos.py](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s03/ex02/comparar_modelos.py)

## Como executar

```powershell
python exercicios/m3s03/ex02/comparar_modelos.py
```

## Comparacao das metricas

### Regressao Linear

- treino: `MAE = 18.5981`
- treino: `RMSE = 27.8897`
- treino: `R2 = 0.9554`
- teste: `MAE = 18.7022`
- teste: `RMSE = 28.0073`
- teste: `R2 = 0.9544`

### Arvore de Decisao

- treino: `MAE = 0.0000`
- treino: `RMSE = 0.0000`
- treino: `R2 = 1.0000`
- teste: `MAE = 11.7172`
- teste: `RMSE = 14.7410`
- teste: `R2 = 0.9874`
- profundidade da arvore: `32`
- numero de folhas: `15110`

## Respostas

### Qual teve melhor desempenho?

A **Arvore de Decisao** teve melhor desempenho no conjunto de teste.

Ela apresentou erro menor (`MAE` e `RMSE`) e `R2` maior do que a Regressao
Linear. Portanto, olhando apenas para a performance preditiva nesta divisao de
treino e teste, a Arvore de Decisao foi superior.

### Qual parece mais confiavel para negocio?

Para negocio, a **Regressao Linear** parece mais confiavel neste momento.

Mesmo tendo desempenho inferior ao da Arvore de Decisao, a Regressao Linear
mostrou comportamento muito estavel entre treino e teste, o que sugere melhor
consistencia. Ja a Arvore de Decisao ajustou perfeitamente o treino
(`R2 = 1.0000` e erro zero), o que pode ser um sinal de **overfitting**.

Alem disso, a Regressao Linear e mais simples de explicar e comunicar para
negocio, o que facilita a interpretacao dos efeitos das variaveis e o uso em
decisoes operacionais.
