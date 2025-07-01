from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Familia(Base):
    __tablename__ = "familias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    descricao = Column(String)

    dinossauros = relationship("Dinossauro", back_populates="familia")


class Dinossauro(Base):
    __tablename__ = "dinossauros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    periodo = Column(String)
    dieta = Column(String)
    imagem_url = Column(String)
    familia_id = Column(Integer, ForeignKey("familias.id"))

    familia = relationship("Familia", back_populates="dinossauros")
