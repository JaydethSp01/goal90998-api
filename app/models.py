from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    name: str
    category: str
    price: float
    stock: int

class Categoria(BaseModel):
    id: int
    name: str

class Talla(BaseModel):
    id: int
    name: str

class Proveedor(BaseModel):
    id: int
    name: str
    contact: str

class Stock(BaseModel):
    product_id: int
    size_id: int
    quantity: int

class Alerta(BaseModel):
    id: int
    product_id: int
    message: str
