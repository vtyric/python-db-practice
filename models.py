import sqlalchemy as sql
import database as _database


class Kofemolka(_database.Base):
    __tablename__ = "kofemolki"
    id = sql.Column(sql.Integer, primary_key=True)
    price = sql.Column(sql.Integer)
    name = sql.Column(sql.String)
