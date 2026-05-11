def validate_invoice(data):

    # =========================
    # ERROR
    # =========================

    if not data:
        return "Error"

    # =========================
    # RECHAZADO
    # =========================

    if data.get("total", 0) <= 0:
        return "Rechazado"

    # =========================
    # REVISIÓN
    # =========================

    if not data.get("fecha"):
        return "Revisión"

    if not data.get("tienda"):
        return "Revisión"

    # =========================
    # PROCESADO
    # =========================

    return "Procesado"