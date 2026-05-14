# M3S03 - Ex02

## Objetivo

Comparar os modelos **Regressão Linear** e **Árvore de Decisão** e responder:

- Qual teve melhor desempenho?
- Qual parece mais confiável para negócio?

## Base de referência

O projeto usa a mesma base local:

`data/raw/dados_AP.csv`

## Arquivo principal

- [comparar_modelos.py](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s03/ex02/comparar_modelos.py)

## Como executar

```powershell
python exercicios/m3s03/ex02/comparar_modelos.py
```

## Comparação das métricas

### Regressão Linear

- treino: `MAE = 18.5981`
- treino: `RMSE = 27.8897`
- treino: `R2 = 0.9554`
- teste: `MAE = 18.7022`
- teste: `RMSE = 28.0073`
- teste: `R2 = 0.9544`

### Árvore de Decisão

- treino: `MAE = 0.0000`
- treino: `RMSE = 0.0000`
- treino: `R2 = 1.0000`
- teste: `MAE = 11.7172`
- teste: `RMSE = 14.7410`
- teste: `R2 = 0.9874`
- profundidade da árvore: `32`
- número de folhas: `15110`

## Respostas

### Qual teve melhor desempenho?

A **Árvore de Decisão** teve melhor desempenho no conjunto de teste.

Ela apresentou erro menor (`MAE` e `RMSE`) e `R2` maior do que a Regressão
Linear. Portanto, olhando apenas para a performance preditiva nesta divisão de
treino e teste, a Árvore de Decisão foi superior.

### Qual parece mais confiável para negócio?

Para negócio, a **Regressão Linear** parece mais confiável neste momento.

Mesmo tendo desempenho inferior ao da Árvore de Decisão, a Regressão Linear
mostrou comportamento muito estável entre treino e teste, o que sugere melhor
consistência. Já a Árvore de Decisão ajustou perfeitamente o treino
(`R2 = 1.0000` e erro zero), o que pode ser um sinal de **overfitting**.

Além disso, a Regressão Linear é mais simples de explicar e comunicar para
negócio, o que facilita a interpretação dos efeitos das variáveis e o uso em
decisões operacionais.
