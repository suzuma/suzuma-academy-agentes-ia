"""Laboratorio 03 - Primer agente con Python."""

def agente(mensaje: str) -> str:
    texto = mensaje.lower().strip()

    if "hola" in texto:
        return "Hola. Soy tu primer agente de IA educativo."
    if "python" in texto:
        return "Python será nuestro lenguaje base para construir los laboratorios."
    if "ayuda" in texto:
        return "Puedo responder preguntas sencillas y demostrar un flujo básico de agente."

    return "Recibí tu mensaje. En este laboratorio todavía no tengo herramientas externas."


def main():
    print("SuZuMa Academy — Agente básico")
    print("Escribe 'salir' para terminar.")

    while True:
        mensaje = input("\nTú: ")

        if mensaje.lower().strip() == "salir":
            print("Agente: Hasta la próxima.")
            break

        print("Agente:", agente(mensaje))


if __name__ == "__main__":
    main()
