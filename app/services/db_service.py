from sqlmodel import Session , select
from app.models.invoice import Invoice, Item
from app.services.category_service import detect_category
from app.services.invoice_validator_service import validate_invoice


def save_invoice(session: Session, data: dict):

    categoria = detect_category(data["tienda"])

    existing_invoice = session.exec(
        select(Invoice).where(
            Invoice.tienda == data.get("tienda"),
            Invoice.total == data.get("total"),
            Invoice.fecha == data.get("fecha")
        )
    ).first()

    if existing_invoice:

        estado = "Duplicado"
    
    else:
        estado = validate_invoice(data)

    invoice = Invoice(
        tienda=data.get("tienda"),
        fecha=data.get("fecha"),
        total=data.get("total"),
        subtotal=data.get("subtotal"),
        iva=data.get("iva"),
        metodo_pago=data.get("metodo de pago"),
        categoria = categoria,
        nombre_archivo=data.get("nombre_archivo"),
        estado=estado
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