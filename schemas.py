import pydantic as pydantic


class KofemolkaCreate(pydantic.BaseModel):
    price: int
    name: str


class Kofemolka(pydantic.BaseModel):
    id: int
    price: int
    name: str
