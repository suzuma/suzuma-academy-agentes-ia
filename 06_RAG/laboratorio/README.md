# Laboratorio 06 — RAG mínimo

## Objetivo

Construir una versión didáctica de recuperación de contexto.

El laboratorio no utiliza embeddings ni una base vectorial todavía. Usa coincidencia sencilla de palabras para hacer visible el flujo:

```text
documentos → búsqueda → contexto → respuesta
```

## Ejecutar

```bash
python rag_minimo.py
```

## Reto

Mejora la recuperación para:

- normalizar texto;
- puntuar coincidencias;
- devolver los 3 fragmentos más relevantes;
- mostrar la fuente utilizada.
