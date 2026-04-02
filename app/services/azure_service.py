import os
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()

endpoint = os.getenv("AZURE_ENDPOINT")
key = os.getenv("AZURE_KEY")

client = DocumentAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)


def analyze_invoice(file_path: str):
    with open(file_path, "rb") as f:
        poller = client.begin_analyze_document(
            model_id="prebuilt-invoice",
            document=f
        )

    result = poller.result()

    if not result.documents:
        return {}

    doc = result.documents[0]

    # 👇 convertir a dict serializable
    parsed = {}

    for key, field in doc.fields.items():
        parsed[key] = field.to_dict()

    return parsed