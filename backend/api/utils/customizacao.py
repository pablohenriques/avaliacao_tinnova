from api.models.models_veiculos import Veiculo


def retornar_lista_parametros(dados: dict) -> list:
    lista_params: list = []

    if dados['veiculo'] is not None:
        param_veiculo = Veiculo.veiculo == dados['veiculo']
        lista_params += param_veiculo

    if dados['marca'] is not None:
        param_marca = Veiculo.marca == dados['marca']
        lista_params.append(param_marca)

    if dados['ano'] is not None:
        param_ano = Veiculo.ano == dados['ano']
        lista_params.append(param_ano)

    if dados['vendido'] is not None:
        param_vendido = Veiculo.vendido == dados['vendido']
        lista_params.append(param_vendido)

    if dados['created'] is not None:
        param_created = Veiculo.created == dados['created']
        lista_params.append(param_created)

    if dados['updated'] is not None:
        param_updated = Veiculo.updated == dados['updated']
        lista_params.append(param_updated)

    return lista_params
