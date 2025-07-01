from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="DinoDex API")

# CORS (caso integre com front futuramente)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependência do DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Recursos Dinossauro
@app.get("/api/recurso1/{dino_id}", response_model=schemas.Dinossauro)
def get_dino(dino_id: int, db: Session = Depends(get_db)):
    return crud.get_dinossauro(db, dino_id)

@app.post("/api/recurso1/", response_model=schemas.Dinossauro)
def post_dino(dino: schemas.DinossauroCreate, db: Session = Depends(get_db)):
    return crud.create_dinossauro(db, dino)

@app.get("/api/recurso2/", response_model=list[schemas.Dinossauro])
def get_all(db: Session = Depends(get_db)):
    return crud.get_all_dinossauros(db)

@app.put("/api/recurso3/{dino_id}", response_model=schemas.Dinossauro)
def put_dino(dino_id: int, dino: schemas.DinossauroUpdate, db: Session = Depends(get_db)):
    return crud.update_dinossauro(db, dino_id, dino)

@app.delete("/api/recurso3/{dino_id}")
def del_dino(dino_id: int, db: Session = Depends(get_db)):
    return crud.delete_dinossauro(db, dino_id)

# Recurso Família
@app.post("/api/recurso4/", response_model=schemas.Familia)
def post_familia(fam: schemas.FamiliaCreate, db: Session = Depends(get_db)):
    return crud.create_familia(db, fam)

@app.get("/api/recurso4/", response_model=list[schemas.Familia])
def get_familias(db: Session = Depends(get_db)):
    return crud.get_all_familias(db)

@app.put("/api/recurso4/{id}", response_model=schemas.Familia)
def put_familia(id: int, fam: schemas.FamiliaUpdate, db: Session = Depends(get_db)):
    return crud.update_familia(db, id, fam)

@app.delete("/api/recurso4/{id}")
def del_familia(id: int, db: Session = Depends(get_db)):
    return crud.delete_familia(db, id)
