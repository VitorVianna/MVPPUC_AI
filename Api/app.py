from flask_openapi3 import OpenAPI, Info, Tag
from flask import Flask, request, send_from_directory, render_template, redirect
from urllib.parse import unquote
from flask_swagger_ui import get_swaggerui_blueprint
from sqlalchemy.exc import IntegrityError
from model import *
from logger import logger
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
creditocliente_tag = Tag(
    name="Credito", description="Envio de dados para buscar informação de Crédito")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.get('/get_credit', tags=[creditocliente_tag])
def get_credit():
    

    try:
        form = Cliente(
            UF = int(request.args.get('estado')),
            IDADE = int(request.args.get('idade')),
            FAIXA_ETARIA = int(request.args.get('faixaEtaria')),
            ESCOLARIDADE = int(request.args.get('escolaridade')),
            ESTADO_CIVIL = int(request.args.get('estadoCivil')),
            QT_FILHOS = int(request.args.get('qtdFilhos')),
            CASA_PROPRIA = int(request.args.get('possuiCasa')),
            VL_IMOVEIS = int(request.args.get('valImoveis')),
            QT_IMOVEIS = int(request.args.get('qtdImoveis')),
            OUTRA_RENDA = int(request.args.get('rendaExtra')),
            OUTRA_RENDA_VALOR = int(request.args.get('valRendaExtra')),
            TEMPO_ULTIMO_EMPREGO_MESES = int(request.args.get('valMesesEmprego')),
            TRABALHANDO_ATUALMENTE = int(request.args.get('trabalha')),
            ULTIMO_SALARIO = float(request.args.get('valSalario')),
            QT_CARROS = int(request.args.get('qtdAutomoveis')),
            VALOR_TABELA_CARROS = int(request.args.get('valAutomoveis'))
            
        )
        # Preparando os dados para o modelo
        X_input = PreProcessador.preparar_form(form)
        # Carregando modelo
        model_path = './MachineLearning/pipelines/pipeline_model.pkl'
        # modelo = Model.carrega_modelo(ml_path)
        modelo = Pipeline.carrega_pipeline(model_path)
        # Realizando a predição
        outcome = int(Model.preditor(modelo, X_input)[0])
        retorno = "Score para o cliente: "+ str(outcome) + "."
        return {"Analise" : retorno + " Recomendamos a disponibilização do crédito" if outcome >= 50 else retorno + "NÃO recomendamos a disponibilização do crédito"}, 200

    except Exception as e:
        error_msg = "Não foi possível executar: " + str(e)
        print(str(e))
        return {"Erro": error_msg + str(e)}, 400
