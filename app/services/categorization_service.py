def categorize_items(items):
    if not items:
        return "otros"

    items_text = " ".join(items).lower()

    if any(x in items_text for x in ["arroz", "leche", "pan"]):
        return "mercado"

    if any(x in items_text for x in ["pizza", "hamburguesa", "combo"]):
        return "restaurante"

    return "otros"