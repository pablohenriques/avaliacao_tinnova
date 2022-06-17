from fastapi import HTTPException
from fastapi.responses import JSONResponse

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "access-control-allow-credentials": "false"
}


def resposta_sucesso(conteudo=None, codigo: int = None) -> JSONResponse:
    if conteudo is None:
        conteudo = 'ok'
    if codigo is None:
        codigo = 201
    return JSONResponse(
        headers=headers,
        content=conteudo,
        status_code=codigo
    )


def resposta_falha(mensagem: str = None, codigo: int = None):
    if (mensagem is None) and (codigo is None):
        mensagem = 'Internal Server Error'
        codigo = 500
    raise HTTPException(
        headers=headers,
        detail=mensagem,
        status_code=codigo
    )
