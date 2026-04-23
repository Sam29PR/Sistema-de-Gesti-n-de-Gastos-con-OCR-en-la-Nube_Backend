from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    valor: float

    invoice_id: Optional[int] = Field(default=None, foreign_key="invoice.id")
    invoice: Optional["Invoice"] = Relationship(back_populates="items")

class Invoice(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tienda: Optional[str]
    fecha: Optional[str]
    total: Optional[float]
    subtotal: Optional[float]
    iva: Optional[float]
    metodo_pago: Optional[str]

    items: List[Item] = Relationship(back_populates="invoice")