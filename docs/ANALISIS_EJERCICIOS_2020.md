# Análisis de `Ejercicios.Python` (Drive)

## Identificación

Origen: carpeta compartida [`Ejercicios.Python`](https://drive.google.com/drive/folders/1-IqZ5lJI79P3rDOXjRQk8CtHG_o902OP). El respaldo exportado de Mi unidad (`Ejercicios.Python-20260829T232548Z-1-001.zip`) contiene los mismos 16 elementos: 15 scripts y el archivo vacío `PracticasBucle1`.

## Qué tipo de material es

No es un proyecto único ni una aplicación lista para publicar. Es un historial de clases/prácticas de Python de 2020, ordenado ahora por tema:

| Área | Evidencia | Lectura para reparación |
|---|---|---|
| Condicionales | Videos 11 y 17, `if/else`, validación de notas y promedios | Ejercicios independientes; conservar las copias porque muestran distintas explicaciones y reescrituras |
| Bucles y generadores | `PracticaBucle2.py`, `PracticasGeneradores.py` | La segunda redefine `generarPares` y `devuelve_ciudades` para mostrar dos técnicas; no debe fusionarse automáticamente |
| Funciones | `PrimerasFunciones.py` | Archivo demostrativo con comentarios y llamadas de ejemplo |
| Colecciones | listas, tuplas y diccionarios | Prácticas sueltas; requieren separar ejemplos de una solución reutilizable |
| Excepciones | `video21/prueba_excepciones.py` | Clase demostrativa con varias versiones de `divide`, bloques comentados y un último ejemplo que pide datos por consola |

## Diagnóstico técnico

- Los 15 scripts copiados pasan análisis sintáctico con Python 3.12.14.
- Varios ejecutan `input()` y `print()` al cargarse; no son módulos importables sin intervención.
- `EjericiciosCondicionales-video11-3.py` redefine `MediaAritmetica` tres veces. La última versión es la que queda activa y usa el contador global `c`.
- `PracticasGeneradores.py` redefine dos veces `generarPares` y dos veces `devuelve_ciudades`; es intencional como comparación de lista/generador y `yield`/`yield from`, pero la última definición sobrescribe la anterior.
- `prueba_excepciones.py` mezcla versiones comentadas/documentales con una ejecución interactiva final; no debe tratarse como una biblioteca.
- No se encontraron `requirements.txt`, pruebas automatizadas, configuración de proyecto ni metadatos Git en esta carpeta.
- `PracticasBucle1` tiene cero bytes. Se registra como evidencia de un archivo creado pero sin contenido recuperable.

## Relación con teoría y trabajos

La carpeta compartida [`Trabajos`](https://drive.google.com/drive/folders/1LRI5-s-ZVXrEoyJbdR_Z7_eOe_ix78dk) contiene siete PDFs (`P1-1` a `P3-2`). Están conservados dentro de `00-originales/mi-unidad/Trabajos-20260829T232953Z-1-001.zip`; se mantienen separados del código para no atribuir consignas o material docente como producción propia. Antes de reparar se debe leer cada PDF y enlazarlo con el ejercicio correspondiente.

## Estrategia recomendada

1. Mantener esta extracción como capa histórica.
2. Crear, en una etapa posterior, una copia didáctica por tema con funciones sin `input()` global y ejemplos bajo `__main__`.
3. No eliminar las redefiniciones: documentar cuál era la versión de cada clase y comparar antes de elegir una solución.
4. Vincular cada copia reparada con el PDF `P1/P2/P3` que corresponda.
5. Esta selección histórica de 15 scripts se publica con procedencia porque fue autorizada expresamente por el titular. La etapa de reparación deberá crear copias didácticas propias y reescritas; no se debe subir material docente ni copias de alumnos como si fueran proyectos propios.

Los archivos recuperados y el manifiesto están en [`../MANIFIESTO.json`](../MANIFIESTO.json). La extracción fue de solo lectura sobre Drive; no se modificó ninguna carpeta remota.
