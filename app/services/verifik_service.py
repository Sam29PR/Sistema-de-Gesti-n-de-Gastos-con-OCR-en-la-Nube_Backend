import requests
import os

VERIFIK_API_KEY = os.getenv("VERIFIK_API_KEY")

def get_company_by_nit(nit: str):
    url = f"https://api.verifik.co/v2/co/companies/{nit}"

    headers = {
        "Authorization": f"Bearer {VERIFIK_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            return {
                "name": data.get("name"),
                "nit": data.get("nit")
            }

        return None

    except Exception as e:
        print("Error Verifik:", e)
        return None