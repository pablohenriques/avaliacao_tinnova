from datetime import datetime
from datetime import timedelta
from sqlalchemy import and_
from sqlalchemy.orm import Session
from api.models.models_veiculos import Veiculo
from api.schemas.schemas_veiculo import SchemaVeiculo
from api.database.basedados import SessionLocal
from api.utils.customizacao import retornar_lista_parametros
from api.utils.conversores import (
    retornar_consulta_em_dict,
    retornar_lista_convertida
)


def criar_sessao_banco_dados() -> Session:
    return SessionLocal()


def fechar_sessao_banco_dados(sessao: Session, objeto=None) -> None:
    sessao.commit()
    if objeto is not None:
        sessao.refresh(objeto)
    sessao.close()


def cadastrar_veiculo_base_dados(dados: SchemaVeiculo) -> None:
    sessao_db: Session = criar_sessao_banco_dados()
    modelo_veiculo: Veiculo = Veiculo(**dados.__dict__)
    modelo_veiculo.created = datetime.now()
    modelo_veiculo.updated = datetime.now()
    sessao_db.add(modelo_veiculo)
    fechar_sessao_banco_dados(sessao_db, modelo_veiculo)
    return None


def retornar_todos_veiculos_base_dados() -> list:
    sessao_db: Session = criar_sessao_banco_dados()
    lista_todos_veiculos: list = sessao_db.query(Veiculo).all()
    lista_convertida: list = retornar_lista_convertida(lista_todos_veiculos)
    fechar_sessao_banco_dados(sessao_db)
    return lista_convertida


def retornar_veiculo_por_id_base_dados(id: int):
    sessao_db: Session = criar_sessao_banco_dados()
    item = sessao_db.query(Veiculo).filter(Veiculo.id == id).first()
    item_convertido = retornar_consulta_em_dict(item)
    fechar_sessao_banco_dados(sessao_db)
    return item_convertido


def consulta_veiculo_parametrizada(dados: dict):
    sessao_db = criar_sessao_banco_dados()
    parametros: list = retornar_lista_parametros(dados)
    consulta = sessao_db.query(Veiculo).filter(and_(*parametros)).all()
    lista_convertida: list = retornar_lista_convertida(consulta)
    fechar_sessao_banco_dados(sessao_db)
    return lista_convertida


def atualizar_veiculo_basedados(id: int, dados_atualizacao: SchemaVeiculo):
    sessao_db = criar_sessao_banco_dados()
    dados_atuais = sessao_db.query(Veiculo).filter(Veiculo.id == id).first()
    dados_atuais.veiculo = dados_atualizacao.veiculo
    dados_atuais.marca = dados_atualizacao.marca
    dados_atuais.ano = dados_atualizacao.ano
    dados_atuais.descricao = dados_atualizacao.descricao
    dados_atuais.vendido = dados_atualizacao.vendido
    dados_atuais.updated = datetime.now()
    fechar_sessao_banco_dados(sessao_db)
    return None


def atualizar_parcial_veiculo_basedados(id: int, dados: SchemaVeiculo):
    db = SessionLocal()
    tabela = db.query(Veiculo).filter(Veiculo.id == id).first()

    if dados.veiculo is not None:
        if dados.veiculo != tabela.veiculo:
            tabela.veiculo = dados.veiculo

    if dados.marca is not None:
        if dados.veiculo != tabela.marca:
            tabela.marca = dados.marca

    if dados.ano is not None:
        if dados.ano != tabela.ano:
            tabela.ano = dados.ano

    if dados.descricao is not None:
        if dados.descricao != tabela.descricao:
            tabela.descricao = dados.descricao

    if dados.vendido is not None:
        if dados.veiculo != tabela.vendido:
            tabela.vendido = dados.vendido

    tabela.updated = datetime.now()
    db.commit()
    db.close()
    return None


def deletar_veiculo_basedados(id: int) -> None:
    sessao_db = criar_sessao_banco_dados()
    sessao_db.query(Veiculo).filter(Veiculo.id == id).delete()
    fechar_sessao_banco_dados(sessao_db)
    return None


def retornar_qtd_carros_por_fabricante() -> list:
    quantidade: dict = {}
    resultado: list = []
    sessao_db = SessionLocal()
    consulta = sessao_db.query(Veiculo).order_by(Veiculo.id)

    for v in consulta:
        if v.marca not in quantidade:
            total: int = (
                sessao_db.query(Veiculo).filter(
                    Veiculo.marca == v.marca).count()
            )
            quantidade[v.marca] = total

    for k, v in quantidade.items():
        item = {'nome': k, 'valor': v}
        resultado.append(item)

    fechar_sessao_banco_dados(sessao_db)
    return resultado


def retornar_cadastro_da_ultima_semana() -> dict:
    sessao_db = criar_sessao_banco_dados()
    ultima_semana = datetime.utcnow() - timedelta(weeks=1)
    condicao_consulta = Veiculo.created > ultima_semana
    total = sessao_db.query(Veiculo).filter(
        and_(condicao_consulta, Veiculo.vendido == True)
    ).count()
    fechar_sessao_banco_dados(sessao_db)
    return total


def retornar_distribuicao_por_decada() -> list:
    categorias: dict = {'2020': 0, '2010': 0, '2000': 0, '1990': 0}
    resultado: list = []
    sessao_db = criar_sessao_banco_dados()
    lista_todos_veiculos: list = sessao_db.query(Veiculo).all()
    for v in lista_todos_veiculos:
        if v.ano >= 2020:
            categorias['2020'] += 1
        elif v.ano >= 2010:
            categorias['2010'] += 1
        elif v.ano >= 2000:
            categorias['2000'] += 1
        elif v.ano >= 1990:
            categorias['1990'] += 1

    for k, v in categorias.items():
        item = {'ano': k, 'valor': v}
        resultado.append(item)

    fechar_sessao_banco_dados(sessao_db)
    return resultado


def retornar_quantidade_veiculos_nao_vendidos() -> int:
    sessao_db = SessionLocal()
    total = sessao_db.query(Veiculo).filter(Veiculo.vendido == False).count()
    fechar_sessao_banco_dados(sessao_db)
    return total
