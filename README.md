# Projeto Analise Preditiva

Projeto minimo em Python para carregar a base CSV e separar:

- `X`: variaveis preditoras
- `y`: variavel resposta

## Estrutura sugerida

```text
projeto_analise_preditiva/
|-- data/
|   |-- raw/
|   |   |-- dados_AP.csv
|-- main.py
|-- requirements.txt
|-- .gitignore
```

## Base utilizada

O projeto espera a base em:

`data/raw/dados_AP.csv`

## Como executar

```powershell
python main.py
```

## Observacao sobre GitHub

O arquivo CSV fica dentro do projeto para facilitar a organizacao local, mas a pasta `data/raw/` foi adicionada ao `.gitignore` para evitar subir a base por engano.
