import sqlalchemy.orm as orm
import database
import models
import schemas


def create_database():
    database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_kofemolki(db: orm.Session):
    return db.query(models.Kofemolka).all()


def get_kofemolka_by_id(db: orm.Session, kofemolka_id: int):
    return db.query(models.Kofemolka).filter(models.Kofemolka.id == kofemolka_id).first()


def create_kofemolka(db: orm.Session, kofemolka: schemas.KofemolkaCreate):
    db_kofemolka = models.Kofemolka(name=kofemolka.name, price=kofemolka.price)
    db.add(db_kofemolka)
    db.commit()


def update_kofemolka(db: orm.Session, kofemolka_id: int, kofemolka: schemas.KofemolkaCreate):
    kofemolka_to_update = get_kofemolka_by_id(db=db, kofemolka_id=kofemolka_id)
    for key, value in kofemolka:
        setattr(kofemolka_to_update, key, value)
    db.commit()


def delete_kofemolka(db: orm.Session, kofemolka_id: int):
    db.query(models.Kofemolka).filter(models.Kofemolka.id == kofemolka_id).delete()
    db.commit()
