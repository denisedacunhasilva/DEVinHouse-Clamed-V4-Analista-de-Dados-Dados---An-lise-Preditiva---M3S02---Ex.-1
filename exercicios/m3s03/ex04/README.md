# M3S03 - Ex04

## Objetivo

Garantir reprodutibilidade no projeto:

- definindo `random_state` na divisão dos dados
- definindo `random_state` nos modelos em que isso se aplica

## O que foi ajustado no projeto

Foi criada uma configuração central em:

- [config.py](/C:/Users/deni_/projeto_analise_preditiva/src/analise_preditiva/config.py)

Com os valores:

- `RANDOM_STATE = 42`
- `TEST_SIZE = 0.2`
- `CV_FOLDS = 5`

Esse `RANDOM_STATE` agora é usado em:

- `train_test_split` na função `dividir_treino_teste`
- `DecisionTreeRegressor` na função `treinar_arvore_decisao`
- `KFold` da validação cruzada da Regressão Linear

Observação:

- a `Regressão Linear` do `scikit-learn` não usa `random_state` nesse caso,
  então a reprodutibilidade dela depende principalmente da divisão dos dados e
  da estratégia de validação cruzada.

## Base de referência

O projeto usa a mesma base local:

`data/raw/dados_AP.csv`

Referência informada no card:

- [Base no Google Drive](https://drive.google.com/file/d/137zf2K5lqh_FAdVKkHiHFPQ6KOJ7gtNq/view?usp=drive_link)

## Respostas

### Por que a reprodutibilidade é importante em projetos reais?

A reprodutibilidade é importante porque garante que o mesmo experimento possa
ser repetido e produza os mesmos resultados quando os dados e as configurações
forem iguais.

Em projetos reais, isso é essencial para:

- validar resultados
- comparar modelos com justiça
- auditar decisões técnicas
- facilitar manutenção e colaboração em equipe
- transmitir mais confiança para negócio e para áreas gestoras

### O que pode acontecer sem esse controle?

Sem controle de reprodutibilidade, o mesmo código pode gerar resultados
diferentes a cada execução.

Isso pode causar problemas como:

- métricas inconsistentes
- dificuldade para depurar erros
- comparações injustas entre modelos
- conclusões erradas sobre desempenho
- perda de confiança no projeto

Em um contexto de negócio, isso pode levar a decisões baseadas em resultados
instáveis, o que aumenta o risco operacional.
