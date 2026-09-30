"""Laboratorio 08 - Equipo multiagente educativo."""

class Investigador:
    def ejecutar(self, tarea):
        return f"Hallazgos iniciales sobre: {tarea}"


class Analista:
    def ejecutar(self, investigacion):
        return f"Análisis realizado a partir de: {investigacion}"


class Redactor:
    def ejecutar(self, analisis):
        return f"Borrador generado a partir de: {analisis}"


class Coordinador:
    def __init__(self):
        self.investigador = Investigador()
        self.analista = Analista()
        self.redactor = Redactor()

    def ejecutar(self, tarea):
        investigacion = self.investigador.ejecutar(tarea)
        analisis = self.analista.ejecutar(investigacion)
        borrador = self.redactor.ejecutar(analisis)

        return {
            "investigacion": investigacion,
            "analisis": analisis,
            "borrador": borrador,
        }


def main():
    coordinador = Coordinador()
    resultado = coordinador.ejecutar("Impacto educativo de los agentes de IA")

    for etapa, contenido in resultado.items():
        print(f"\n{etapa.upper()}:")
        print(contenido)


if __name__ == "__main__":
    main()
