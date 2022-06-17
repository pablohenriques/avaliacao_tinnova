from api.models.models_veiculos import Veiculo


def retornar_consulta_em_dict(objeto: Veiculo) -> dict:
    dicionario = {'id': int(objeto.id), 'veiculo': objeto.veiculo,
                  'marca': objeto.marca, 'ano': objeto.ano,
                  'descricao': objeto.descricao, 'vendido': objeto.vendido,
                  'created': objeto.created.strftime('%Y-%m-%dT%H:%M:%S.%f'),
                  'updated': objeto.updated.strftime('%Y-%m-%dT%H:%M:%S.%f')}
    return dicionario


def retornar_lista_convertida(lista_objetos) -> list:
    lista: list = []
    for objeto in lista_objetos:
        objeto_convertido = retornar_consulta_em_dict(objeto)
        lista.append(objeto_convertido)
    return lista
