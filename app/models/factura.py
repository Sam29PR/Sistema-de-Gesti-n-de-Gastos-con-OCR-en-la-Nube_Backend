from pydantic import BaseModel
from typing import List, Optional


class Item(BaseModel):
    nombre: Optional[str] = None
    cantidad: Optional[float] = None
    precio: Optional[float] = None


class Factura(BaseModel):
    nit: Optional[str] = None
    establecimiento: Optional[str] = None
    fecha: Optional[str] = None
    total: Optional[float] = None
    iva: Optional[float] = None
    metodo_pago: Optional[str] = None
    items: Optional[List[Item]] = None