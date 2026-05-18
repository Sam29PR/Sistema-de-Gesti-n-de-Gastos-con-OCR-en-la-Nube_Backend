def get_invoice_state(data, is_duplicate=False):

    # 🔴 1. DUPLICADO (PRIORIDAD MÁXIMA)
    if is_duplicate:
        return "Duplicado"

    # 🔴 2. ERROR
    if not data:
        return "Error"

    # 🔴 3. VALIDACIÓN TOTAL
    try:
        total = float(data.get("total") or 0)
    except:
        return "Error"

    # 🔴 4. RECHAZADO
    if total <= 0:
        return "Rechazado"

    # 🔴 5. REVISIÓN
    if not data.get("tienda") or not data.get("fecha"):
        return "Revisión"

    # 🟢 6. PROCESADO
    return "Procesado"