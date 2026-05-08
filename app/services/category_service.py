CATEGORY_RULES = {

    # =========================
    # COMIDA Y RESTAURANTES
    # =========================
    "Restaurantes": [
        "mcdonalds",
        "burger king",
        "kfc",
        "subway",
        "dominos",
        "pizza hut",
        "little caesars",
        "starbucks",
        "juan valdez",
        "crepes",
        "kokoriko",
        "el corral",
        "presto",
        "frisby",
        "popsy",
        "sandwich qbano",
        "bbc",
        "buffalo wings",
        "sushi",
        "taco",
        "burger",
        "pizza",
        "cafe",
        "restaurant",
        "restaurante",
        "asados",
        "parrilla",
        "pollo",
        "comidas rapidas"
    ],

    # =========================
    # SUPERMERCADOS
    # =========================
    "Supermercado": [
        "d1",
        "ara",
        "olimpica",
        "exito",
        "carulla",
        "makro",
        "pricesmart",
        "jumbo",
        "supertiendas",
        "megatiendas",
        "justo y bueno",
        "mercado",
        "supermercado",
        "tienda",
        "minimarket"
    ],

    # =========================
    # TECNOLOGÍA
    # =========================
    "Tecnología": [
        "apple",
        "amazon",
        "samsung",
        "xiaomi",
        "huawei",
        "lenovo",
        "hp",
        "dell",
        "asus",
        "acer",
        "microsoft",
        "sony",
        "playstation",
        "xbox",
        "nintendo",
        "steam",
        "epic games",
        "gamepass",
        "alkosto",
        "ktronix",
        "tecnologia",
        "pc",
        "computador",
        "laptop",
        "celular"
    ],

    # =========================
    # HOGAR
    # =========================
    "Hogar": [
        "homecenter",
        "sodimac",
        "ikea",
        "easy",
        "ferreteria",
        "muebles",
        "colchon",
        "electrohogar",
        "decoracion",
        "hogar",
        "pinturas",
        "ceramica",
        "Jamar",
    ],

    # =========================
    # TRANSPORTE
    # =========================
    "Transporte": [
        "uber",
        "cabify",
        "didi",
        "indrive",
        "taxi",
        "terpel",
        "shell",
        "esso",
        "texaco",
        "copec",
        "gasolina",
        "peaje",
        "transmetro",
        "metro",
        "bus",
        "rapi taxi"
    ],

    # =========================
    # SALUD
    # =========================
    "Salud": [
        "farmatodo",
        "cruz verde",
        "olimpica drogueria",
        "drogueria",
        "farmacia",
        "eps",
        "clinica",
        "hospital",
        "laboratorio",
        "odontologia",
        "medicina",
        "salud total",
        "sanitas",
        "sura",
        "colsanitas"
    ],

    # =========================
    # EDUCACIÓN
    # =========================
    "Educación": [
        "universidad",
        "colegio",
        "udemy",
        "coursera",
        "platzi",
        "domestika",
        "crehana",
        "sena",
        "educacion",
        "instituto",
        "escuela",
        "matricula",
        "biblioteca"
    ],

    # =========================
    # ENTRETENIMIENTO
    # =========================
    "Entretenimiento": [
        "netflix",
        "spotify",
        "disney",
        "hbo",
        "prime video",
        "youtube",
        "cine",
        "cinemark",
        "procinal",
        "royal films",
        "steam",
        "epic games",
        "twitch",
        "xbox",
        "playstation"
    ],

    # =========================
    # ROPA Y MODA
    # =========================
    "Ropa y Moda": [
        "zara",
        "pull and bear",
        "bershka",
        "nike",
        "adidas",
        "puma",
        "h&m",
        "forever 21",
        "shein",
        "studio f",
        "koaj",
        "arturo calle",
        "patprimo",
        "ropa",
        "zapatos",
        "tenis",
        "moda"
    ],

    # =========================
    # BANCOS Y FINANZAS
    # =========================
    "Finanzas": [
        "bancolombia",
        "nequi",
        "davivienda",
        "daviplata",
        "bbva",
        "nu bank",
        "nu",
        "scotiabank",
        "itau",
        "banco de bogota",
        "western union",
        "paypal",
        "payu",
        "mercadopago",
        "efecty"
    ],

    # =========================
    # SERVICIOS
    # =========================
    "Servicios": [
        "air-e",
        "triple a",
        "movistar",
        "claro",
        "tigo",
        "wom",
        "etb",
        "directv",
        "internet",
        "agua",
        "energia",
        "gas",
        "telefono",
        "wifi",
        "plan movil"
    ],

    # =========================
    # VIAJES
    # =========================
    "Viajes": [
        "avianca",
        "latam",
        "jetsmart",
        "wingo",
        "despegar",
        "booking",
        "airbnb",
        "hotel",
        "hostal",
        "resort",
        "turismo",
        "viajes",
        "aeropuerto"
    ],

    # =========================
    # MASCOTAS
    # =========================
    "Mascotas": [
        "veterinaria",
        "petshop",
        "mascota",
        "dog",
        "cat",
        "purina",
        "agrocampo",
        "pet food",
        "animal",
        "veterinario"
    ],

    # =========================
    # DEPORTES Y FITNESS
    # =========================
    "Deportes": [
        "smart fit",
        "bodytech",
        "gym",
        "gimnasio",
        "sportline",
        "decathlon",
        "under armour",
        "fitness",
        "crossfit",
        "yoga",
        "pilates"
    ],

    # =========================
    # BELLEZA
    # =========================
    "Belleza": [
        "peluqueria",
        "barberia",
        "spa",
        "nails",
        "maquillaje",
        "cosmeticos",
        "belleza",
        "salon",
        "barber shop"
    ],

    # =========================
    # CONSTRUCCIÓN
    # =========================
    "Construcción": [
        "cemento",
        "arena",
        "bloque",
        "construccion",
        "obra",
        "ferreteria",
        "materiales"
    ],

    # =========================
    # IMPUESTOS Y GOBIERNO
    # =========================
    "Impuestos": [
        "dian",
        "impuesto",
        "tributo",
        "alcaldia",
        "gobierno",
        "transito",
        "simit"
    ]

}

import re


def clean_text(text: str):

    text = text.lower().strip()

    # elimina símbolos raros
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # elimina saltos de línea dobles y espacios extra
    text = re.sub(r'\s+', ' ', text)

    return text

def detect_category(store_name: str):

    if not store_name:
        return "Otros"

    store_name = clean_text(store_name)

    print("TIENDA LIMPIA:", store_name)

    for category, keywords in CATEGORY_RULES.items():

        for keyword in keywords:

            keyword = clean_text(keyword)

            if keyword in store_name:
                print("MATCH:", keyword, "=>", category)
                return category

    return "Otros"