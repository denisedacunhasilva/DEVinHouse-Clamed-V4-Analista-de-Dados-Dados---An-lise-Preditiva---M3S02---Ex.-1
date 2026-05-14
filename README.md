# DEVinHouse Clamed V4 - Análise Preditiva

Repositório com exercícios da trilha Analista de Dados do DEVinHouse Clamed V4,
focado em análise preditiva com Python, pandas e scikit-learn.

Este projeto organiza os exercícios por módulo e por exercício, separando
respostas teóricas, scripts de modelagem e funções reutilizáveis.

## Estrutura atual

```text
projeto_analise_preditiva/
|-- data/
|   |-- raw/
|   |   |-- dados_AP.csv
|   |-- README.md
|-- exercicios/
|   |-- m3s01/
|   |   |-- ex01/
|   |   |   |-- README.md
|   |   |-- ex02/
|   |   |   |-- README.md
|   |   |-- ex03/
|   |   |   |-- README.md
|   |   |-- ex04/
|   |   |   |-- README.md
|   |-- m3s02/
|   |   |-- ex01/
|   |   |   |-- README.md
|   |   |   |-- separar_xy.py
|   |   |-- ex02/
|   |   |   |-- README.md
|   |   |   |-- train_test_split.py
|   |   |-- ex03/
|   |   |   |-- README.md
|   |   |   |-- metricas_regressao.py
|   |   |-- ex04/
|   |   |   |-- README.md
|   |-- m3s03/
|   |   |-- ex01/
|   |   |   |-- README.md
|   |   |   |-- decision_tree_regressor.py
|   |   |-- ex02/
|   |   |   |-- README.md
|   |   |   |-- comparar_modelos.py
|   |   |-- ex03/
|   |   |   |-- README.md
|   |   |   |-- cross_validation_regressao_linear.py
|   |   |-- ex04/
|   |   |   |-- README.md
|-- src/
|   |-- analise_preditiva/
|   |   |-- __init__.py
|   |   |-- config.py
|   |   |-- data_utils.py
|   |   |-- model_utils.py
|-- main.py
|-- requirements.txt
|-- .gitignore
```

## Como o projeto foi organizado

- `src/analise_preditiva/`: funções compartilhadas entre os exercícios.
- `src/analise_preditiva/config.py`: configurações centrais de reprodutibilidade.
- `exercicios/m3s01/`: exercícios teóricos e interpretativos.
- `exercicios/m3s02/ex01/`: código para separação de `X` e `y`.
- `exercicios/m3s02/ex02/`: código da divisão treino/teste com `train_test_split`.
- `exercicios/m3s02/ex03/`: métricas de avaliação do modelo de regressão.
- `exercicios/m3s02/ex04/`: interpretação das métricas do `Ex03`.
- `exercicios/m3s03/ex01/`: segundo modelo com `DecisionTreeRegressor`.
- `exercicios/m3s03/ex02/`: comparação entre Regressão Linear e Árvore de Decisão.
- `exercicios/m3s03/ex03/`: validação cruzada da Regressão Linear com `cross_val_score`.
- `exercicios/m3s03/ex04/`: garantia de reprodutibilidade e resposta conceitual.
- `data/raw/`: base local usada no projeto.

## Base de dados

O projeto espera a base neste caminho:

`data/raw/dados_AP.csv`

## Ambiente virtual

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Como executar

Fluxo geral do projeto:

```powershell
python main.py
```

M3S02 Exercício 1:

```powershell
python exercicios/m3s02/ex01/separar_xy.py
```

M3S02 Exercício 2:

```powershell
python exercicios/m3s02/ex02/train_test_split.py
```

M3S02 Exercício 3:

```powershell
python exercicios/m3s02/ex03/metricas_regressao.py
```

M3S02 Exercício 4:

- [Resposta do Ex04](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s02/ex04/README.md)

M3S03 Exercício 1:

```powershell
python exercicios/m3s03/ex01/decision_tree_regressor.py
```

M3S03 Exercício 2:

```powershell
python exercicios/m3s03/ex02/comparar_modelos.py
```

M3S03 Exercício 3:

```powershell
python exercicios/m3s03/ex03/cross_validation_regressao_linear.py
```

M3S03 Exercício 4:

- [Resposta do Ex04](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s03/ex04/README.md)

Respostas teóricas de M3S01:

- [Ex01](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s01/ex01/README.md)
- [Ex02](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s01/ex02/README.md)
- [Ex03](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s01/ex03/README.md)
- [Ex04](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s01/ex04/README.md)

## Boas práticas para os próximos exercícios

- Crie uma nova pasta para cada exercício, por exemplo `ex03/`, `ex04/`.
- Deixe em `src/` apenas o que for reutilizável.
- Guarde respostas teóricas em `README.md` dentro da pasta do exercício.
- Evite caminhos absolutos no código.
- Mantenha a base fora do GitHub quando ela não puder ser publicada.
