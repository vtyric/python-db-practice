from typing import List
import sqlalchemy.orm as orm
from fastapi import HTTPException
import services, schemas, os, fastapi
from database import DATABASE_NAME
from web_parser import load_kofemolki_data

app = fastapi.FastAPI()

if not os.path.exists(DATABASE_NAME):
    services.create_database()
    load_kofemolki_data()


@app.get("/kofemolki/", response_model=List[schemas.Kofemolka])
def get_kofemolki(db: orm.Session = fastapi.Depends(services.get_db)):
    return services.get_kofemolki(db=db)


@app.get("/kofemolki/{kofemolki_id}", response_model=schemas.Kofemolka)
def get_kofemolka(kofemolka_id: int, db: orm.Session = fastapi.Depends(services.get_db)):
    kofemolka = services.get_kofemolka_by_id(db=db, kofemolka_id=kofemolka_id)
    if kofemolka is None:
        raise HTTPException(status_code=400, detail="Отсутствует кофемолка с таким индексомы")
    return kofemolka


@app.post("/kofemolki/")
def create_kofemolka(kofemolka: schemas.KofemolkaCreate, db: orm.Session = fastapi.Depends(services.get_db)):
    services.create_kofemolka(db=db, kofemolka=kofemolka)
    return {"status": "ok"}


@app.put("/kofemolki/{kofemolki_id}")
def update_kofemolka(kofemolka_id: int, kofemolka: schemas.KofemolkaCreate,
                     db: orm.Session = fastapi.Depends(services.get_db)):
    kofemolka = services.update_kofemolka(db=db, kofemolka_id=kofemolka_id, kofemolka=kofemolka)
    return {"status": "ok"}


@app.delete("/kofemolki/{kofemolki_id}")
def update_kofemolka(kofemolka_id: int, db: orm.Session = fastapi.Depends(services.get_db)):
    services.delete_kofemolka(db=db, kofemolka_id=kofemolka_id)
    return {"status": "ok"}
