from sqlalchemy.orm import Session
import models, schemas

# Recurso 1 - GET by ID e POST
def get_dinossauro(db: Session, dino_id: int):
    return db.query(models.Dinossauro).filter(models.Dinossauro.id == dino_id).first()

def create_dinossauro(db: Session, dino: schemas.DinossauroCreate):
    db_dino = models.Dinossauro(**dino.dict())
    db.add(db_dino)
    db.commit()
    db.refresh(db_dino)
    return db_dino

# Recurso 2 - GET All
def get_all_dinossauros(db: Session):
    return db.query(models.Dinossauro).all()

# Recurso 3 - PUT e DELETE
def update_dinossauro(db: Session, dino_id: int, dino: schemas.DinossauroUpdate):
    db_dino = get_dinossauro(db, dino_id)
    if db_dino:
        for key, value in dino.dict().items():
            setattr(db_dino, key, value)
        db.commit()
        db.refresh(db_dino)
    return db_dino

def delete_dinossauro(db: Session, dino_id: int):
    db_dino = get_dinossauro(db, dino_id)
    if db_dino:
        db.delete(db_dino)
        db.commit()
    return db_dino

# Recurso 4 - Família (CRUD completo)
def create_familia(db: Session, familia: schemas.FamiliaCreate):
    db_fam = models.Familia(**familia.dict())
    db.add(db_fam)
    db.commit()
    db.refresh(db_fam)
    return db_fam

def get_all_familias(db: Session):
    return db.query(models.Familia).all()

def update_familia(db: Session, id: int, fam: schemas.FamiliaUpdate):
    db_fam = db.query(models.Familia).filter(models.Familia.id == id).first()
    if db_fam:
        for key, value in fam.dict().items():
            setattr(db_fam, key, value)
        db.commit()
        db.refresh(db_fam)
    return db_fam

def delete_familia(db: Session, id: int):
    db_fam = db.query(models.Familia).filter(models.Familia.id == id).first()
    if db_fam:
        db.delete(db_fam)
        db.commit()
    return db_fam
