from core.schemas.empresa import EmpresaSchema
from core.models.empresa import EmpresaModel
from sqlalchemy.orm import Session
from core.models.dao import SessionLocal, Dao
import json

db : Session = SessionLocal()
dao = Dao()

class EmpresaController:
    
    def __init__(self):
        pass

    def criar_empresa(self, nova_empresa: EmpresaSchema):
        db_empresa = EmpresaModel(**nova_empresa.__dict__)
        dao.insert_data(db_empresa)
        return None

    def listar_empresas(self):
        return dao.get_todas_empresa(EmpresaModel)

    def empresa_mais_antiga(self):
        empresa = dao.get_empresa_mais_antiga(EmpresaModel)
        nome = empresa['nome']
        return nome

    def maior_num_funcionarios(self):
        return dao.get_num_funcionarios_regiao(EmpresaModel)

    def total_funcionarios(self):
        return dao.get_total_funcionarios(EmpresaModel)

    def regiao_industrial(self):
        return dao.get_regiao_industrial(EmpresaModel)