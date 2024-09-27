# API de Cálculo de Score utilizando Inteligência Artificial
Este projeto foi desenvolvido como MVP para a Disciplina **Qualidade de Software, Segurança e Sistemas Inteligentes**

O objetivo foi desenvolver uma Machine Learning, uma API e um Front utilizando Python para calcular o Score de um determinado cliente para Bancos.

Os notebooks estão localizados na pasta **Api/MachineLearning/notebooks/**
Também localizados em:
> [ESSI_MVP-PUC-AI.ipynb](https://colab.research.google.com/drive/1n-Q8xlqkEDxzEEwr6WFWwO3rQYHxcV-i?usp=drive_link)
> Realiza o tratamento dos dados, e cria os arquivos model.pkl, X_test_dataset_model.csv e y_test_dataset_model.csv

> [MVP-PUC-AI.ipynb](https://colab.research.google.com/drive/1_GK3txfanYfKa_4SXTzYDDsC6SDUXuRO?usp=drive_link)
> Realiza o tratamento dos dados, e apresenta os diferentes tipos de algoritmos, bem como suas respostas aos testes de aprendizagem.

O CSV contendo o Dataset está na pasta: **Api/MachineLearning/data/dados_credito.csv**
Onde encontramos uma lista de informações de clientes e seus Scores.

O FrontEnd foi desenvolvido utilizando HTML, JavaScript e Bootstrap.
O BackEnd foi desenvolvido utilizando Python, e as bibliotecas Flask e Scikit-Learn principalmente.

## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas, é bem simples o processo.

Após clonar o repositório, é necessário ir ao diretório raiz do projeto, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

> O BackEnd está na pasta API, sendo assim, antes de executar o comando para criar o ambiente virtual, certifique-se de que está executando na pasta, caso não esteja, utilize o comando: > cd Api
> python -m venv env
> env/Scripts/Activate.ps1  

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

Após se certificar de que a API está rodando corretamente, abra, no navegador o arquivo de FrontEnd, localizado na pasta Web/index.html.
Ou clique com o botão direito do mouse no arquivo index.html, e clique na opção Open With Live Server (Necessário possuir a extensão Live Server intalada no seu VS Code).

## Demonstração
Vídeo de demonstração: [Clique Aqui](https://photos.app.goo.gl/TQSohEzJgEvt1bLS7)
