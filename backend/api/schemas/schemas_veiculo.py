from datetime import datetime
from pydantic import BaseModel


class SchemaVeiculo(BaseModel):
    veiculo: str = None
    marca: str = None
    ano: int = None
    descricao: str = None
    vendido: bool = None
    created: datetime = None
    updated: datetime = None

    class Config:
        orm_mode = True
