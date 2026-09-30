"""Laboratorio 05 - Herramientas y Tool Calling."""

from datetime import datetime


def hora_actual():
    return datetime.now().strftime("%H:%M:%S")


def sumar(a, b):
    return a + b


def buscar_concepto(concepto):
    conceptos = {
        "rag": "RAG permite recuperar información externa para aportar contexto a una respuesta.",
        "agente": "Un agente combina un modelo con instrucciones, estado y capacidades para realizar tareas.",
        "tool calling": "Tool Calling permite solicitar la ejecución estructurada de una herramienta."
    }
    return conceptos.get(concepto.lower(), "Concepto no encontrado.")


TOOLS = {
    "hora_actual": hora_actual,
    "sumar": sumar,
    "buscar_concepto": buscar_concepto,
}


def ejecutar_herramienta(nombre, **parametros):
    herramienta = TOOLS.get(nombre)

    if herramienta is None:
        raise ValueError(f"Herramienta no registrada: {nombre}")

    return herramienta(**parametros)


def main():
    print("SuZuMa Academy — Tool Calling")
    print("Ejemplos:")
    print("  hora")
    print("  sumar 8 7")
    print("  concepto rag")
    print("  salir")

    while True:
        entrada = input("\nTú: ").strip()

        if entrada.lower() == "salir":
            break

        partes = entrada.split()

        if partes[0].lower() == "hora":
            print("Agente:", ejecutar_herramienta("hora_actual"))

        elif partes[0].lower() == "sumar" and len(partes) == 3:
            print("Agente:", ejecutar_herramienta("sumar", a=float(partes[1]), b=float(partes[2])))

        elif partes[0].lower() == "concepto" and len(partes) >= 2:
            concepto = " ".join(partes[1:])
            print("Agente:", ejecutar_herramienta("buscar_concepto", concepto=concepto))

        else:
            print("Agente: No pude identificar una herramienta para esa solicitud.")


if __name__ == "__main__":
    main()
