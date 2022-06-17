from datetime import datetime
from fastapi import APIRouter
from api.schemas.schemas_veiculo import SchemaVeiculo
from api.controller.controller_veiculos import *


router = APIRouter(tags=['veiculo'])


@router.post('/')
async def cadastrar(dados: SchemaVeiculo):
    return cadastrar_veiculo(dados)


@router.get('/')
async def consultar(
        veiculo: str = None,
        marca: str = None,
        ano: int = None,
        vendido: bool = None,
        created: datetime = None,
        updated: datetime = None
):
    dados = {
        'veiculo': veiculo,
        'marca': marca,
        'ano': ano,
        'vendido': vendido,
        'created': created,
        'updated': updated
    }
    return retornar_todos_veiculos(dados)


@router.get('/dados')
async def retornar_dados():
    return retornar_dados_sobre_veiculos()


@router.get('/{id}')
async def consultar_por_id(id: int):
    return consultar_veiculo(id)


@router.put('/{id}')
async def atualizar_completo(id: int, dados: SchemaVeiculo):
    return atualizar_veiculo(id, dados)


@router.patch('/{id}')
async def atualizar_parcialmente(id: int, dados: SchemaVeiculo):
    return atualizar_veiculo_parcial(id, dados)


@router.delete('/{id}')
async def deletar(id: int):
    return deletar_veiculo(id)
