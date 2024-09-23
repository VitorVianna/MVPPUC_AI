from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "./MachineLearning/data/test_dataset_model.csv"
colunas = ['UF','IDADE','ESCOLARIDADE','ESTADO_CIVIL','QT_FILHOS','CASA_PROPRIA','QT_IMOVEIS','VL_IMOVEIS','OUTRA_RENDA','OUTRA_RENDA_VALOR','TEMPO_ULTIMO_EMPREGO_MESES',
           'TRABALHANDO_ATUALMENTE','ULTIMO_SALARIO','QT_CARROS','VALOR_TABELA_CARROS','SCORE','FAIXA_ETARIA']

# Carga dos dados
dataset = Carregador.carregar_dados(url_dados, colunas)
array = dataset.values
X = array[:,0:-1]
y = array[:,-1]
    
# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo_lr():  
    # Importando o modelo de regressão logística
    lr_path = './MachineLearning/models/model.pkl'
    modelo_lr = Model.carrega_modelo(lr_path)

    # Obtendo as métricas da Regressão Logística
    acuracia_lr = Avaliador.avaliar(modelo_lr, X, y)
    
    # Testando as métricas da Regressão Logística 
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_lr >= 0.78 
    # assert recall_lr >= 0.5 
    # assert precisao_lr >= 0.5 
    # assert f1_lr >= 0.5 
 
