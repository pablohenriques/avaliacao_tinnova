from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.types import DateTime
from api.database.basedados import Base


class Veiculo(Base):

    __tablename__ = 'veiculos'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    veiculo = Column(String(255))
    marca = Column(String(255))
    ano = Column(Integer)
    descricao = Column(Text)
    vendido = Column(Boolean)
    created = Column(DateTime)
    updated = Column(DateTime)

    def __repr__(self):
        detalhes: str = None
        detalhes += f' id: {int(self.id)}.'
        detalhes += f' veiculo: {self.veiculo}.'
        detalhes += f' marca: {self.marca}.'
        detalhes += f' ano: {self.ano}.'
        return f'<{detalhes}>'
