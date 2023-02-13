from fastapi import APIRouter

from core.schemas.empresa import EmpresaSchema
from core.controller.empresa import EmpresaController
from core.http.response import success_response

router = APIRouter(
    prefix="/empresa",
    tags=["empresa"]
)

empresa_controller = EmpresaController()

@router.post("/criar")
def criar_empresa(nova_empresa: EmpresaSchema):
    empresa_controller.criar_empresa(nova_empresa)
    return success_response()

@router.get("/listar")
def listar_empresas():
    return success_response(empresa_controller.listar_empresas())

@router.get("/regiao-maior-num-funcionarios")
def maior_num_funcionarios():
    return success_response(empresa_controller.maior_num_funcionarios())

@router.get("/mais-antiga")
def empresa_mais_antiga():
    return success_response(empresa_controller.empresa_mais_antiga())

@router.get("/total-funcionarios")
def total_funcionarios():
    return success_response(empresa_controller.total_funcionarios())

@router.get("/regiao-industrial")
def regiao_industrial():
    return success_response(empresa_controller.regiao_industrial())