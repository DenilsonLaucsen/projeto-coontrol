from pydantic import BaseModel
from datetime import date

class EmpresaSchema(BaseModel):
    nome:               str = None
    dataFundacao:       date = None
    qtdFuncionarios:    int = None
    regiao:             str = None
    setor:              str = None

    class Config:
        orm_mode = True