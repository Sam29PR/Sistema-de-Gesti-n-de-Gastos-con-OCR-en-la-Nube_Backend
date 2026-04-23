from sqlmodel import Session
from app.models.invoice import Invoice, Item


def save_invoice(session: Session, data: dict):
    invoice = Invoice(
        tienda=data.get("tienda"),
        fecha=data.get("fecha"),
        total=data.get("total"),
        subtotal=data.get("subtotal"),
        iva=data.get("iva"),
        metodo_pago=data.get("metodo de pago"),
    )

    session.add(invoice)
    session.commit()
    session.refresh(invoice)

    #  guardar items
    items = data.get("items", [])

    for item in items:
        db_item = Item(
            description=item.get("description"),
            valor=item.get("valor"),
            invoice_id=invoice.id
        )
        session.add(db_item)

    session.commit()

    return invoice