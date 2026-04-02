def normalize_invoice(fields: dict):
    def get_amount(field):
        try:
            return field["value"]["amount"]
        except:
            return None

    def get_items(items_field):
        items = []

        if not items_field or not items_field.get("value"):
            return items

        for item in items_field["value"]:
            data = item.get("value", {})

            description = data.get("Description", {}).get("value")
            amount = get_amount(data.get("Amount", {}))

            items.append({
                "description": description,
                "valor": amount
            })

        return items

    normalized = {
        "total": get_amount(fields.get("InvoiceTotal", {})),
        "subtotal": get_amount(fields.get("SubTotal", {})),
        "iva": get_amount(fields.get("TotalTax", {})),
        "items": get_items(fields.get("Items", {})),
    }

    return normalized