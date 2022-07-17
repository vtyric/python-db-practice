import sqlalchemy.orm as orm
import services, schemas, os, fastapi
from database import DATABASE_NAME
from web_parser import load_kofemolki_data

app = fastapi.FastAPI()

if not os.path.exists(DATABASE_NAME):
    services.create_database()
    load_kofemolki_data()


@app.get("/kofemolki/")
def get_kofemolki(db: orm.Session = fastapi.Depends(services.get_db)):
    return services.get_kofemolki(db=db)


@app.get("/kofemolki/{kofemolki_id}")
def get_kofemolka(kofemolka_id: int, db: orm.Session = fastapi.Depends(services.get_db)):
    return services.get_kofemolka_by_id(db=db, kofemolka_id=kofemolka_id)


@app.post("/kofemolki/")
def create_kofemolka(kofemolka: schemas.KofemolkaCreate, db: orm.Session = fastapi.Depends(services.get_db)):
    services.create_kofemolka(db=db, kofemolka=kofemolka)
    return {"status": "ok"}


@app.put("/kofemolki/{kofemolki_id}")
def update_kofemolka(kofemolka_id: int, kofemolka: schemas.KofemolkaCreate,
                     db: orm.Session = fastapi.Depends(services.get_db)):
    services.update_kofemolka(db=db, kofemolka_id=kofemolka_id, kofemolka=kofemolka)
    return {"status": "ok"}


@app.delete("/kofemolki/{kofemolki_id}")
def update_kofemolka(kofemolka_id: int, db: orm.Session = fastapi.Depends(services.get_db)):
    services.delete_kofemolka(db=db, kofemolka_id=kofemolka_id)
    return {"status": "ok"}
