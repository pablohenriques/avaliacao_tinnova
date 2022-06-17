# Documentação
---

## Execícios 1 a 4
---
-   A resolução dos exercícios 1, 2, 3 e 4 estão disponíveis no formato notebook python (.ipynb). Os arquivos podem ser testados no Google Colab ou ferramentas públicas para execução do notebook.
- Jupyter: https://jupyter.org/try-jupyter/lab/ (obs: nesta ferramenta, as primeiras execuções do notebook podem demorar alguns segundos)

## Execício 5
---
### Online:
- Tanto o site quanto a API do exercício 5 estão disponíveis nos links:
- Frontend: https://tinfrontapp.herokuapp.com/dados
- Backend: https://tinapiprojeto.herokuapp.com
- Ambas aplicações foram disponibilizadas no Heroku, inclusive utilizando o banco de dados Postgres, também fornecido pelo Heroku.


### Local (Backend)
- Python: 3.8. Framework: FastAPI. SO: Linux Mint
- Para executar localmente a API, acesse a pasta /backend
- Crie o ambiente virtual: 
```python3 
python3 -m venv venv
```
- Instale as dependências: 
```python3
pip install -r requirements.txt
```
- Execute o main.py 
```python3
python3 main.py
```
- Obs.: No arquivo main.py é possível alterar a porta para evitar conflitos na execução.

### Local (Frontend)
- Node: 16. Framework: VueJS. SO: Linux Mint
- Para executar o frontend, acesse /frontend/app
- Execute o comando:
```nodejs
npm install
```
- Após concluir a instalaão das dependências, execute:
```nodejs
npm run serve
```
- A aplicação deverá ser executada localmente em um porta escolhida pela aplicação.


## Outras plataformas
- Python
    - Windows/MacOS/Linux: https://pip.pypa.io/en/stable/installation/

- Node:
    - Windows/MacOS/Linux: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
