# Adaptador para modelos reales

Los laboratorios pueden evolucionar desde implementaciones locales hacia un proveedor real de modelos.

Para evitar acoplar el curso a un único proveedor, se utiliza una interfaz mínima basada en variables de entorno.

## Variables

```text
LLM_API_URL=
LLM_API_KEY=
LLM_MODEL=
```

Nunca coloques valores reales en GitHub.

## Ejemplo de configuración local

Copia `.env.example` como `.env` y completa los valores en tu equipo.

El cliente usa la biblioteca estándar de Python para realizar una petición HTTP y devuelve el texto de la respuesta cuando el proveedor utiliza un formato compatible con el adaptador.

Cada proveedor puede requerir un pequeño ajuste de payload o extracción de respuesta.
