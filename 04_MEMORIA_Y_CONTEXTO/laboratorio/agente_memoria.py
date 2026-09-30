"""Laboratorio 04 - Memoria y contexto."""

class Memoria:
    def __init__(self, limite=10):
        self.mensajes = []
        self.limite = limite

    def agregar(self, rol, contenido):
        self.mensajes.append({"rol": rol, "contenido": contenido})
        self.mensajes = self.mensajes[-self.limite:]

    def contexto(self):
        return list(self.mensajes)


class Agente:
    def __init__(self):
        self.memoria = Memoria()

    def responder(self, mensaje):
        self.memoria.agregar("usuario", mensaje)

        if "me llamo" in mensaje.lower():
            respuesta = "Perfecto. Recordaré tu nombre durante esta sesión."
        elif "qué recuerdas" in mensaje.lower():
            datos = self.memoria.contexto()
            respuesta = f"Recuerdo {len(datos)} mensajes en esta sesión."
        else:
            respuesta = f"Procesé tu mensaje dentro de un contexto de {len(self.memoria.contexto())} elementos."

        self.memoria.agregar("agente", respuesta)
        return respuesta


def main():
    agente = Agente()
    print("SuZuMa Academy — Agente con memoria")
    print("Escribe 'salir' para terminar.")

    while True:
        mensaje = input("\nTú: ")

        if mensaje.lower().strip() == "salir":
            break

        print("Agente:", agente.responder(mensaje))


if __name__ == "__main__":
    main()
