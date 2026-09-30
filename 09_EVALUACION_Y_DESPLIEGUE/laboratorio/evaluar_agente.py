"""Laboratorio 09 - Evaluación y observabilidad educativa."""

def agente(mensaje):
    if "hola" in mensaje.lower():
        return "Hola. Soy un agente educativo."
    if "python" in mensaje.lower():
        return "Python es nuestro lenguaje de laboratorio."
    return "No tengo una respuesta específica."


CASOS = [
    {
        "entrada": "hola",
        "esperado": "Hola. Soy un agente educativo.",
    },
    {
        "entrada": "háblame de python",
        "esperado": "Python es nuestro lenguaje de laboratorio.",
    },
]


def evaluar():
    resultados = []

    for caso in CASOS:
        obtenido = agente(caso["entrada"])
        ok = obtenido == caso["esperado"]

        resultados.append({
            "entrada": caso["entrada"],
            "esperado": caso["esperado"],
            "obtenido": obtenido,
            "ok": ok,
        })

    return resultados


def main():
    resultados = evaluar()
    aprobados = sum(1 for r in resultados if r["ok"])
    total = len(resultados)

    for resultado in resultados:
        print(resultado)

    print(f"\nResultado: {aprobados}/{total} casos correctos.")


if __name__ == "__main__":
    main()
