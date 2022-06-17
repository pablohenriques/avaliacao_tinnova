from starlette.responses import JSONResponse
from api.schemas.schemas_veiculo import SchemaVeiculo
from api.utils.resposta_http import resposta_sucesso, resposta_falha
from api.utils.verificadores import verificar_objeto_esta_nulo
from api.database.gerenciador import *


def cadastrar_veiculo(dados: SchemaVeiculo):
    try:
        cadastrar_veiculo_base_dados(dados)
        return resposta_sucesso()
    except Exception as e:
        print(f'Erro - Controller Cadastrar Veiculo: {e}')
    return resposta_falha('Bad Request', 400)


def retornar_todos_veiculos(dados: dict) -> JSONResponse:
    verificao_objeto = verificar_objeto_esta_nulo(dados)

    if verificao_objeto:
        try:
            consulta = consulta_veiculo_parametrizada(dados)
            return resposta_sucesso(consulta, 200)
        except Exception as e:
            print(f'Erro - Controller Consulta Veiculo Parametros: {e}')
        return resposta_falha()
    else:
        try:
            consulta = retornar_todos_veiculos_base_dados()
            return resposta_sucesso(consulta, 200)
        except Exception as e:
            print(f'Erro - Controller Reotonar Todos Veiculos: {e}')
        return resposta_falha()


def consultar_veiculo(id: int) -> JSONResponse:
    try:
        consulta = retornar_veiculo_por_id_base_dados(id)
        return resposta_sucesso(consulta, 200)
    except Exception as e:
        print(f'Erro - Controller Consultar Veiculo Por Id: {e}')
    return resposta_falha()


def atualizar_veiculo(id: int, dados: SchemaVeiculo) -> JSONResponse:
    try:
        atualizar_veiculo_basedados(id, dados)
        return resposta_sucesso(codigo=200)
    except Exception as e:
        print(f'Erro - Controller Atualizar Veiculo: {e}')
    return resposta_falha()


def atualizar_veiculo_parcial(id: int, dados: SchemaVeiculo) -> JSONResponse:
    try:
        atualizar_parcial_veiculo_basedados(id, dados)
        return resposta_sucesso(codigo=200)
    except Exception as e:
        print(f'Erro - Controller Atualizar Parcialemte Veiculo: {e}')
    return resposta_falha()


def deletar_veiculo(id: int) -> JSONResponse:
    try:
        deletar_veiculo_basedados(id)
        return resposta_sucesso(codigo=200)
    except Exception as e:
        print(f'Erro - Controller Deletar Veiculo: {e}')
    resposta_falha()


def retornar_dados_sobre_veiculos() -> JSONResponse:
    try:
        carros_fabricante: dict = retornar_qtd_carros_por_fabricante()
        carros_semana: dict = retornar_cadastro_da_ultima_semana()
        carros_decada: dict = retornar_distribuicao_por_decada()
        nao_vendidos: int = retornar_quantidade_veiculos_nao_vendidos()
        dados: dict = {
            'quantidade_fabricante': carros_fabricante,
            'quantidade_semana': carros_semana,
            'quantidade_decada': carros_decada,
            'quantidade_nao_vendida': nao_vendidos
        }

        return resposta_sucesso(dados, 200)
    except Exception as e:
        print(f'Erro - Controller Dados Veiculo: {e}')
    resposta_falha()
