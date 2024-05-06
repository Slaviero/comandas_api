import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer

# ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'

    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(CHAR(200), nullable=False)
    valor_unitario = Column(float(11,2), unique=True, nullable=False)
    foto = Column(CHAR(100), nullable=False)
   
    def __init__(self, id_produto, nome, descricao, valor_unitario, foto):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.valor_unitario = valor_unitario
        self.foto = foto