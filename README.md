# Projeto Analise Preditiva

Repositorio organizado para crescer por modulo e por exercicio, sem misturar
codigo reutilizavel com entregas pontuais da disciplina.

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
|   |   |   |-- cross_validation_regressao_linear.py
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
|   |   |-- ex04/
|   |   |   |-- README.md
|-- src/
|   |-- analise_preditiva/
|   |   |-- __init__.py
|   |   |-- config.py
|   |   |-- data_utils.py
|-- main.py
|-- requirements.txt
|-- .gitignore
```

## Como o projeto foi separado

- `src/analise_preditiva/`: funcoes compartilhadas entre exercicios.
- `src/analise_preditiva/config.py`: configuracoes centrais de reproducibilidade.
- `exercicios/m3s01/`: exercicios teoricos e interpretativos.
- `exercicios/m3s02/ex01/`: codigo para separacao de `X` e `y`.
- `exercicios/m3s02/ex02/`: codigo da divisao treino/teste com `train_test_split`.
- `exercicios/m3s02/ex03/`: metricas de avaliacao do modelo de regressao.
- `exercicios/m3s02/ex04/`: interpretacao das metricas do `Ex03`.
- `exercicios/m3s03/ex01/`: segundo modelo com `DecisionTreeRegressor`.
- `exercicios/m3s03/ex02/`: comparacao entre Regressao Linear e Arvore de Decisao.
- `exercicios/m3s03/ex03/`: validacao cruzada da Regressao Linear com `cross_val_score`.
- `exercicios/m3s03/ex04/`: garantia de reproducibilidade e resposta conceitual.
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

Exercicio 1:

```powershell
python exercicios/m3s02/ex01/separar_xy.py
```

Exercicio 2:

```powershell
python exercicios/m3s02/ex02/train_test_split.py
```

Exercicio 3:

```powershell
python exercicios/m3s02/ex03/metricas_regressao.py
```

Exercicio 4:

- [Resposta do Ex04](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s02/ex04/README.md)

M3S03 Exercicio 1:

```powershell
python exercicios/m3s03/ex01/decision_tree_regressor.py
```

M3S03 Exercicio 2:

```powershell
python exercicios/m3s03/ex02/comparar_modelos.py
```

M3S03 Exercicio 3:

```powershell
python exercicios/m3s03/ex03/cross_validation_regressao_linear.py
```

M3S03 Exercicio 4:

- [Resposta do Ex04](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s03/ex04/README.md)

Respostas teoricas de M3S01:

- [Ex01](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s01/ex01/README.md)
- [Ex02](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s01/ex02/README.md)
- [Ex03](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s01/ex03/README.md)
- [Ex04](/C:/Users/deni_/projeto_analise_preditiva/exercicios/m3s01/ex04/README.md)

## Boas praticas para os proximos exercicios

- Crie uma nova pasta para cada exercicio, por exemplo `ex03/`, `ex04/`.
- Deixe em `src/` apenas o que for reutilizavel.
- Guarde respostas teoricas em `README.md` dentro da pasta do exercicio.
- Evite caminhos absolutos no codigo.
- Mantenha a base fora do GitHub quando ela nao puder ser publicada.
