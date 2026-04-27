from sqlmodel import SQLModel
from typing import List, Optional


class ItemRead(SQLModel):
    id: int
    description: str
    valor: float   


class FacturaPublic(SQLModel):
    id: int
    tienda: Optional[str]
    fecha: Optional[str]
    total: Optional[float]
    subtotal: Optional[float]
    iva: Optional[float]
    metodo_pago: Optional[str]

    items: List[ItemRead] = []