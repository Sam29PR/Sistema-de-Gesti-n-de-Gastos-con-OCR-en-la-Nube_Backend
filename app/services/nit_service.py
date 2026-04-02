def categorize_nit(nit):
    if not nit:
        return "desconocido"

    if nit.startswith("890"):
        return "gran_contribuyente"

    return "general"