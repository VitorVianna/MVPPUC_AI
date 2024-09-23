from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = ['UF','IDADE','ESCOLARIDADE','ESTADO_CIVIL','QT_FILHOS','CASA_PROPRIA','QT_IMOVEIS','VL_IMOVEIS','OUTRA_RENDA','OUTRA_RENDA_VALOR','TEMPO_ULTIMO_EMPREGO_MESES',
#           'TRABALHANDO_ATUALMENTE','ULTIMO_SALARIO','QT_CARROS','VALOR_TABELA_CARROS','SCORE','FAIXA_ETARIA']

class Cliente(Base):
    __tablename__ = 'clientes'
    ID = Column(Integer, primary_key=True)
    UF = Column("UF", Integer)
    IDADE= Column("IDADE", Integer)
    ESCOLARIDADE = Column("ESCOLARIDADE", Integer)
    ESTADO_CIVIL = Column("ESTADO_CIVIL", Integer)
    QT_FILHOS = Column("QT_FILHOS", Integer)
    CASA_PROPRIA = Column("CASA_PROPRIA", Integer)
    QT_IMOVEIS = Column("QT_IMOVEIS", Integer)
    VL_IMOVEIS = Column("VL_IMOVEIS", Integer)
    OUTRA_RENDA = Column("OUTRA_RENDA", Integer)
    OUTRA_RENDA_VALOR = Column("OUTRA_RENDA_VALOR", Integer)
    TEMPO_ULTIMO_EMPREGO_MESES = Column("TEMPO_ULTIMO_EMPREGO_MESES", Integer)
    TRABALHANDO_ATUALMENTE = Column("TRABALHANDO_ATUALMENTE", Integer)
    ULTIMO_SALARIO = Column("ULTIMO_SALARIO", Float)
    QT_CARROS = Column("QT_CARROS", Integer)
    VALOR_TABELA_CARROS = Column("VALOR_TABELA_CARROS", Integer)
    SCORE = Column("SCORE", Integer)
    FAIXA_ETARIA = Column("FAIXA_ETARIA", Integer)
    
    def __init__(self, UF:int,IDADE:int,ESCOLARIDADE:int,ESTADO_CIVIL:int,QT_FILHOS:int,CASA_PROPRIA:int,QT_IMOVEIS :int,VL_IMOVEIS:int,OUTRA_RENDA :int,OUTRA_RENDA_VALOR:int,
                 TEMPO_ULTIMO_EMPREGO_MESES :int,TRABALHANDO_ATUALMENTE :int,ULTIMO_SALARIO :float,QT_CARROS :int,VALOR_TABELA_CARROS :int,FAIXA_ETARIA:int ):
        """
        Dados do Cliente

        Arguments:
        UF 
        IDADE
        ESCOLARIDADE 
        ESTADO_CIVIL
        QT_FILHOS 
        CASA_PROPRIA 
        QT_IMOVEIS 
        VL_IMOVEIS 
        OUTRA_RENDA 
        OUTRA_RENDA_VALOR 
        TEMPO_ULTIMO_EMPREGO_MESES 
        TRABALHANDO_ATUALMENTE 
        ULTIMO_SALARIO 
        QT_CARROS 
        VALOR_TABELA_CARROS 
        FAIXA_ETARIA 
        """
        self.UF =UF
        self.IDADE =IDADE
        self.ESCOLARIDADE =ESCOLARIDADE
        self.ESTADO_CIVIL=ESTADO_CIVIL
        self.QT_FILHOS =QT_FILHOS
        self.CASA_PROPRIA= CASA_PROPRIA
        self.QT_IMOVEIS =QT_IMOVEIS
        self.VL_IMOVEIS =VL_IMOVEIS
        self.OUTRA_RENDA =OUTRA_RENDA
        self.OUTRA_RENDA_VALOR= OUTRA_RENDA_VALOR
        self.TEMPO_ULTIMO_EMPREGO_MESES= TEMPO_ULTIMO_EMPREGO_MESES
        self.TRABALHANDO_ATUALMENTE =TRABALHANDO_ATUALMENTE
        self.ULTIMO_SALARIO =ULTIMO_SALARIO
        self.QT_CARROS =QT_CARROS
        self.VALOR_TABELA_CARROS =VALOR_TABELA_CARROS
        self.FAIXA_ETARIA =FAIXA_ETARIA
