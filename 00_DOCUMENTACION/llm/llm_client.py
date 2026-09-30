"""Cliente mínimo para un endpoint de modelos configurable.

No contiene claves ni credenciales.
Ajusta payload/extracción si tu proveedor utiliza otro contrato HTTP.
"""

import json
import os
from urllib.request import Request, urlopen


class LLMClient:
    def __init__(self):
        self.url = os.getenv("LLM_API_URL", "").strip()
        self.api_key = os.getenv("LLM_API_KEY", "").strip()
        self.model = os.getenv("LLM_MODEL", "").strip()

        if not self.url:
            raise ValueError("Falta LLM_API_URL.")
        if not self.api_key:
            raise ValueError("Falta LLM_API_KEY.")
        if not self.model:
            raise ValueError("Falta LLM_MODEL.")

    def generate(self, prompt):
        payload = {
            "model": self.model,
            "input": prompt,
        }

        request = Request(
            self.url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
            method="POST",
        )

        with urlopen(request, timeout=60) as response:
            data = json.loads(response.read().decode("utf-8"))

        # Algunos proveedores devuelven "output_text".
        if isinstance(data.get("output_text"), str):
            return data["output_text"]

        # Otros pueden devolver una respuesta estructurada.
        if isinstance(data.get("text"), str):
            return data["text"]

        raise ValueError(
            "El proveedor respondió, pero el formato no coincide con este adaptador. "
            "Revisa la respuesta y adapta la extracción."
        )
