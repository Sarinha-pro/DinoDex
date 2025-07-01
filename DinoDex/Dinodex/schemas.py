from pydantic import BaseModel
from typing import Optional

class DinossauroBase(BaseModel):
    nome: str
    periodo: Optional[str]
    dieta: Optional[str]
    imagem_url: Optional[str]
    familia_id: int

class DinossauroCreate(DinossauroBase):
    pass

class DinossauroUpdate(DinossauroBase):
    pass

class Dinossauro(DinossauroBase):
    id: int
    class Config:
        orm_mode = True


class FamiliaBase(BaseModel):
    nome: str
    descricao: Optional[str]

class FamiliaCreate(FamiliaBase):
    pass

class FamiliaUpdate(FamiliaBase):
    pass

class Familia(FamiliaBase):
    id: int
    class Config:
        orm_mode = True
