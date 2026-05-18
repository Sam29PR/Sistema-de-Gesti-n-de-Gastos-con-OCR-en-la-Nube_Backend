from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
import os

router = APIRouter()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class AIRequest(BaseModel):
    total: float
    categories: list
    stores: list


def mock_insights(data: AIRequest):
    return {
        "insights": f"""
🟡 MODO GRATIS (SIMULADO)

1. Tu gasto total fue de {data.total}. Revisa si es alto para tu presupuesto.

2. La categoría más frecuente parece ser: {data.categories[0] if data.categories else 'no definida'}.

3. Se detectan compras en: {', '.join(data.stores) if data.stores else 'tiendas no registradas'}.

4. Recomendación: reduce compras impulsivas y controla gastos diarios.
"""
    }


@router.post("/insights")
def generate_insights(data: AIRequest):

    try:
        prompt = f"""
        Eres un analista financiero experto.

        Analiza estos gastos:
        - Total: {data.total}
        - Categorías: {data.categories}
        - Tiendas: {data.stores}

        Devuelve 4 insights cortos y accionables en español.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un analista financiero experto"},
                {"role": "user", "content": prompt}
            ]
        )

        return {
            "insights": response.choices[0].message.content,
            "mode": "ai"
        }

    except Exception as e:
        print("OpenAI error:", e)

        return {
            **mock_insights(data),
            "mode": "mock"
        }