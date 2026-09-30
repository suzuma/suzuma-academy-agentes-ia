"""Laboratorio 06 - RAG mínimo educativo."""

DOCUMENTOS = [
    {
        "id": "doc-01",
        "titulo": "Agentes de IA",
        "texto": "Un agente puede combinar un modelo, instrucciones, estado y herramientas para realizar tareas."
    },
    {
        "id": "doc-02",
        "titulo": "RAG",
        "texto": "RAG recupera información relevante de una colección de documentos y la incorpora como contexto."
    },
    {
        "id": "doc-03",
        "titulo": "Tool Calling",
        "texto": "Una herramienta permite que el sistema solicite la ejecución de una función con parámetros estructurados."
    },
]


def recuperar(consulta):
    palabras = set(consulta.lower().split())
    resultados = []

    for documento in DOCUMENTOS:
        texto = documento["texto"].lower()
        puntuacion = sum(1 for palabra in palabras if palabra in texto)

        if puntuacion:
            resultados.append((puntuacion, documento))

    resultados.sort(key=lambda item: item[0], reverse=True)
    return [documento for _, documento in resultados]


def responder(consulta):
    documentos = recuperar(consulta)

    if not documentos:
        return "No encontré contexto relevante en los documentos disponibles."

    contexto = "\n".join(
        f"[{doc['id']}] {doc['texto']}" for doc in documentos[:2]
    )

    return (
        "Respuesta basada en el contexto recuperado:\n"
        f"{contexto}\n\n"
        f"Fuentes: {', '.join(doc['id'] for doc in documentos[:2])}"
    )


def main():
    print("SuZuMa Academy — RAG mínimo")
    print("Escribe 'salir' para terminar.")

    while True:
        consulta = input("\nPregunta: ")

        if consulta.lower().strip() == "salir":
            break

        print(responder(consulta))


if __name__ == "__main__":
    main()
