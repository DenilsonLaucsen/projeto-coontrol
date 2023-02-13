from sqlalchemy import create_engine, asc, func, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://testeCoontrol:testeCoontrol@db:5432/testeCoontrol"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_database():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Error: {e}")

class Dao:

    def __init__(self) -> None:
        self.db = SessionLocal()

    def insert_data(self, values):
        self.db.add(values)
        self.db.commit()
        self.db.refresh(values)
        self.db.close()

    def get_todas_empresa(self, model):
        db_all_data = self.db.query(model)
        self.db.close()
        tmp_list = []
        for item in db_all_data:
            tmp_list.append(item.as_dict())
        return tmp_list

    def get_empresa_mais_antiga(self, model):
        db_empresa = self.db.query(model).order_by(asc(model.dataFundacao)).first()
        self.db.close()
        return db_empresa.as_dict()

    def get_num_funcionarios_regiao(self, model):
        num_funcionarios = self.db.query(func.sum(model.qtdFuncionarios), model.regiao)\
                                    .group_by(model.regiao)\
                                    .order_by(desc(func.sum(model.qtdFuncionarios))).first()
        self.db.close()

        info = {
                'numFuncionarios': num_funcionarios[0],
                'regiao': num_funcionarios[1]
            }
        return info

    def get_total_funcionarios(self, model):
        num_funcionarios = self.db.query(func.sum(model.qtdFuncionarios)).first()
        return num_funcionarios[0]

    def get_regiao_industrial(self, model):
        regiao = self.db.query(func.count(model.nome), model.regiao)\
                            .filter(model.setor == "Industrial")\
                            .group_by(model.regiao)\
                            .order_by(desc(func.count(model.nome))).first()
        return regiao[1]