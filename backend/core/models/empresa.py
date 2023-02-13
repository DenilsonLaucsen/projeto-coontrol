from sqlalchemy import Column, Integer, String, Date

from core.models.dao import Base

class EmpresaModel(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    dataFundacao = Column(Date)
    qtdFuncionarios = Column(Integer)
    regiao = Column(String)
    setor = Column(String)

    def as_dict(self):
       return {
           'id': self.id,
           'nome': self.nome,
           'dataFundacao': str(self.dataFundacao),
           'qtdFuncionarios': self.qtdFuncionarios,
           'regiao': self.regiao,
           'setor': self.setor
       }
    
    def __repr__(self) -> str:
        return f"id: {self.id}, nome: {self.nome}, dataFundacao: {self.dataFundacao}, qtdFuncionarios: {self.qtdFuncionarios}, regiao: {self.regiao}, setor: {self.setor}"