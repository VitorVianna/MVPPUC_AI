from flask_openapi3 import OpenAPI, Info, Tag
from flask import Flask, request, send_from_directory, render_template, redirect
from flask_swagger_ui import get_swaggerui_blueprint
from sqlalchemy.exc import IntegrityError
from model import Session
from datetime import datetime
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
    session = Session()

    try:
        estado = request.args.get('estado')
        idade = request.args.get('idade')
        faixaEtaria = request.args.get('faixaEtaria')
        escolaridade = request.args.get('escolaridade')
        estadoCivil = request.args.get('estadoCivil')
        qtdFilhos = request.args.get('qtdFilhos')
        possuiCasa = request.args.get('possuiCasa')
        valImoveis = request.args.get('valImoveis')
        qtdImoveis = request.args.get('qtdImoveis')
        rendaExtra = request.args.get('rendaExtra')
        valRendaExtra = request.args.get('valRendaExtra')
        valMesesEmprego = request.args.get('valMesesEmprego')
        trabalha = request.args.get('trabalha')
        valSalario = request.args.get('valSalario')
        qtdAutomoveis = request.args.get('qtdAutomoveis')
        valAutomoveis = request.args.get('valAutomoveis')
        return {"credit": estado + ","+ idade + ","+faixaEtaria+","+escolaridade+","+estadoCivil+","+qtdFilhos
                +","+possuiCasa+","+valImoveis+","+qtdImoveis+","+rendaExtra+","+valRendaExtra+","+valMesesEmprego+","+trabalha+","+
                valSalario+","+qtdAutomoveis+","+valAutomoveis}, 200

    except Exception as e:
        error_msg = "Não foi possível executar: " + str(e)
        print(str(e))
        return {"Erro": error_msg + str(e)}, 400
