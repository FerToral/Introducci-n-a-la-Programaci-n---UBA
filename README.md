# Introducción a la Programación — UBA

Ejercicios y apuntes de programación de la Facultad de Ciencias Exactas y Naturales de la Universidad de Buenos Aires, correspondientes al segundo cuatrimestre de 2025.

La materia trabaja con programación funcional e imperativa. Por el momento, este repositorio reúne una selección de ejercicios de la etapa imperativa en Python: funciones, estructuras de control, listas, matrices, pilas, colas y diccionarios. La colección es parcial; no representa todas las actividades de la cursada.

## Guías

| Guía | Temas incluidos | Código | Pruebas |
|---|---|---|---|
| [Guía 6](Guias/Guia-06) | Funciones, condicionales, ciclos y alcance de variables | [src](Guias/Guia-06/src) | [tests](Guias/Guia-06/tests) |
| [Guía 7](Guias/Guia-07) | Listas, cadenas y matrices | [src](Guias/Guia-07/src) | [tests](Guias/Guia-07/tests) |
| [Guía 8](Guias/Guia-08) | Pilas, colas y diccionarios; ejercicios 1–18 | [src](Guias/Guia-08/src) | [tests](Guias/Guia-08/tests) |

Cada guía conserva junto al código su descripción, alcance y referencias al material teórico correspondiente del [campus de la materia](https://campus.exactas.uba.ar/course/view.php?id=674). Los enlaces del campus pueden requerir iniciar sesión.

## Ejecutar las pruebas

Se utiliza Python 3.12 y la biblioteca estándar, sin dependencias adicionales. Desde la raíz del repositorio, en PowerShell:

```powershell
$env:PYTHONPATH = "Guias/Guia-06/src"
python -m unittest discover -s Guias/Guia-06/tests -p "test_*.py"
$env:PYTHONPATH = "Guias/Guia-07/src"
python -m unittest discover -s Guias/Guia-07/tests -p "test_*.py"
$env:PYTHONPATH = "Guias/Guia-08/src"
python -m unittest discover -s Guias/Guia-08/tests -p "test_*.py"
Remove-Item Env:PYTHONPATH
```

Las pruebas comprueban los casos implementados y sus regresiones. No constituyen una corrección oficial ni garantizan la cobertura de todos los ejercicios de cada guía.
