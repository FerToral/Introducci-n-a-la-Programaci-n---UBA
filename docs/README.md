# Colab: variantes de Introducción a Python

Origen: carpeta compartida [`Colab Notebooks`](https://drive.google.com/drive/folders/14V9vu3OL7Gm6NCZsVLZ5Wmjt4qTDC_DE). Se descargaron nueve notebooks, conservando el ID de Drive en el nombre para distinguir copias.

## Hallazgos

- Cuatro variantes de `DibujarGrilla` tienen exactamente 7 celdas, 4 de código y el mismo hash de fuentes (`9b238b44c98e4642`): son duplicados históricos, no cuatro proyectos distintos.
- `Fernando T. Clase 1` contiene 124 celdas (57 de código, 67 de teoría) y es el material más claramente asociado a tu cursada; incluye ejercicios de funciones, divisores, promedios y primalidad.
- `Copia de Clase 2` contiene 171 celdas y mezcla teoría, ejercicios y salidas; sus celdas 58, 74 y 77 no son Python válido aislado, probablemente por comandos o fragmentos de notebook.
- Las dos copias de `Clase 3` tienen la misma estructura (120 celdas), pero diferentes fuentes/salidas; ambas deben conservarse hasta comparar qué versión corresponde a cada momento.
- `Cuaderno de pruebas` contiene 78 celdas y una celda con anotación inválida; es un espacio experimental, no un módulo listo para publicar.
- Los cuatro `DibujarGrilla` importan `folium`, `matplotlib` y `pandas`; las dependencias deberán documentarse antes de reparar o ejecutar fuera de Colab.

## Criterio de reparación

Los notebooks son evidencia de trabajo y material teórico, no se convierten automáticamente en `.py`. Primero se comparan variantes por celdas y salidas; después se pueden extraer ejercicios propios a módulos con funciones puras, pruebas y un `requirements.txt` separado. Las salidas guardadas y el texto docente se conservan para reconstruir la relación entre explicación y ejercicio.

Ver [`MANIFIESTO_COLAB.json`](MANIFIESTO_COLAB.json) para IDs, tamaños, cantidad de celdas y diagnóstico sintáctico por notebook.
