from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

from backend.app.models.invoice import Invoice


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    valor: float

    invoice_id: Optional[int] = Field(default=None, foreign_key="invoice.id")
    invoice: Optional["Invoice"] = Relationship(back_populates="items")