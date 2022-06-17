def verificar_objeto_esta_nulo(parametros: dict):
    for _, valor in parametros.items():
        if valor is not None:
            return True
    return False
