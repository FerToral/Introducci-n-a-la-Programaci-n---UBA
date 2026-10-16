# Python UBA y ejercicios históricos de Drive

Esta selección reúne código, no material nominal de evaluación. `src/uba/` conserva las copias históricas de las guías 6–8; `reparaciones/` contiene las variantes ya corregidas sin reemplazar los originales; `src/drive-2020/` contiene los 15 scripts de práctica recuperados de `Ejercicios.Python`.

La teoría, consignas, tests y variantes completas permanecen en el archivo de la cursada. `docs/` contiene índices y análisis para reconstruir la relación curso → tema → ejercicio. Antes de publicar se revisará la licencia de PDFs y se excluirán DNI, reportes privados, planillas y soluciones docentes.

Estado: selección curada en la rama `codex/uba-python-curation`. Se publican fuentes propias/históricas y reparaciones identificadas; no se publican PDFs, planillas, reportes nominales ni soluciones docentes.

## Estructura

- `src/uba/`: copias históricas de las guías 6–8.
- `reparaciones/`: versiones corregidas de Guía 7 y Guía 8, con sus pruebas.
- `src/drive-2020/`: ejercicios Python recuperados de Drive, conservados como colección histórica.
- `docs/`: procedencia, análisis y relación entre teoría y ejercicios.

## Validación local

Con Python 3.12 se verificó la sintaxis de los 22 archivos incluidos. Las reparaciones tienen pruebas separadas: Guía 7 (45 pruebas al incluir regresión e históricos; 23 de regresión) y Guía 8 (9 pruebas), todas aprobadas en la selección local. Los ejercicios históricos de Drive no se presentan como una aplicación única.

Para ejecutar las pruebas desde la raíz:

```powershell
$env:PYTHONPATH = "reparaciones/guia-07/src"
python -m unittest discover -s reparaciones/guia-07/tests -p "*.py"
$env:PYTHONPATH = "reparaciones/guia-08/src"
python -m unittest discover -s reparaciones/guia-08/tests -p "*.py"
```

La publicación mantiene el criterio de procedencia: la consigna oficial del campus es la autoridad para el curso 2C2025; las referencias públicas sirven sólo para contraste.

Para reparar sin subir código histórico por error, se usará como criterio adicional la [comparación de referencias públicas UBA](../../../auditoria-github-2026-10-06/REFERENCIAS_PUBLICAS_UBA_Y_CRITERIO_REPARACION_2026-10-16.md). El curso completo del campus sigue siendo la autoridad para Python 2C2025; las referencias externas sólo sirven para contraste.
