# M3S03 - Ex04

## Objetivo

Garantir reprodutibilidade no projeto:

- definindo `random_state` na divisao dos dados
- definindo `random_state` nos modelos em que isso se aplica

## O que foi ajustado no projeto

Foi criada uma configuracao central em:

- [config.py](/C:/Users/deni_/projeto_analise_preditiva/src/analise_preditiva/config.py)

Com os valores:

- `RANDOM_STATE = 42`
- `TEST_SIZE = 0.2`
- `CV_FOLDS = 5`

Esse `RANDOM_STATE` agora e usado em:

- `train_test_split` na funcao `dividir_treino_teste`
- `DecisionTreeRegressor` na funcao `treinar_arvore_decisao`
- `KFold` da validacao cruzada da Regressao Linear

Observacao:

- a `Regressao Linear` do `scikit-learn` nao usa `random_state` nesse caso,
  entao a reprodutibilidade dela depende principalmente da divisao dos dados e
  da estrategia de validacao cruzada.

## Base de referencia

O projeto usa a mesma base local:

`data/raw/dados_AP.csv`

Referencia informada no card:

- [Base no Google Drive](https://drive.google.com/file/d/137zf2K5lqh_FAdVKkHiHFPQ6KOJ7gtNq/view?usp=drive_link)

## Respostas

### Por que a reprodutibilidade e importante em projetos reais?

A reprodutibilidade e importante porque garante que o mesmo experimento possa
ser repetido e produza os mesmos resultados quando os dados e as configuracoes
forem iguais.

Em projetos reais, isso e essencial para:

- validar resultados
- comparar modelos com justica
- auditar decisoes tecnicas
- facilitar manutencao e colaboracao em equipe
- transmitir mais confianca para negocio e para areas gestoras

### O que pode acontecer sem esse controle?

Sem controle de reprodutibilidade, o mesmo codigo pode gerar resultados
diferentes a cada execucao.

Isso pode causar problemas como:

- metricas inconsistentes
- dificuldade para depurar erros
- comparacoes injustas entre modelos
- conclusoes erradas sobre desempenho
- perda de confianca no projeto

Em um contexto de negocio, isso pode levar a decisoes baseadas em resultados
instaveis, o que aumenta o risco operacional.
