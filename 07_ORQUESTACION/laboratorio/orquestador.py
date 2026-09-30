"""Laboratorio 07 - Orquestación educativa."""

def investigar():
    return "Investigación completada"


def analizar():
    return "Análisis completado"


def redactar():
    return "Redacción completada"


TOOLS = {
    "investigar": investigar,
    "analizar": analizar,
    "redactar": redactar,
}


def ejecutar_plan(plan):
    estado = []

    for paso in plan:
        nombre = paso["accion"]
        funcion = TOOLS[nombre]

        try:
            resultado = funcion()
            estado.append({
                "accion": nombre,
                "estado": "ok",
                "resultado": resultado,
            })
        except Exception as error:
            estado.append({
                "accion": nombre,
                "estado": "error",
                "error": str(error),
            })
            break

    return estado


def main():
    plan = [
        {"accion": "investigar"},
        {"accion": "analizar"},
        {"accion": "redactar"},
    ]

    for item in ejecutar_plan(plan):
        print(item)


if __name__ == "__main__":
    main()
