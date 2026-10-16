# Introducción a la Programación — UBA

Repositorio personal de la cursada de Introducción a la Programación de la UBA, segundo cuatrimestre de 2025. El contenido está organizado por cursada, guía y tipo de material; las prácticas históricas de Drive 2020 se mantienen en un bloque separado porque no pertenecen automáticamente a la cursada 2025.

## Estructura del repositorio

```text
cursada-uba-2025-2c/
└── guias/
    ├── guia-06/
    │   └── codigo/
    ├── guia-07/
    │   ├── codigo-historico/
    │   ├── codigo/
    │   └── pruebas/
    └── guia-08/
        ├── codigo-historico/
        ├── codigo/
        └── pruebas/

practicas-python-2020/
├── condicionales/
├── bucles-y-generadores/
├── funciones/
├── colecciones/
└── excepciones/

docs/
├── cursada-uba-2025-2c/
└── archivo-historico-drive.md
```

`codigo-historico/` conserva las versiones originales de las guías 7 y 8. `codigo/` contiene la implementación que se valida con las pruebas; no se reemplazó ni se borró el material histórico.

`practicas-python-2020/` es un archivo independiente de 15 ejercicios recuperados de Drive. Se publican con su procedencia y no se presentan como parte de la cursada UBA 2025 ni como una aplicación única.

## Validación

Con Python 3.12 se verificó la sintaxis de los 28 archivos Python. Las pruebas de la cursada ejecutan:

- Guía 7: 45 pruebas aprobadas.
- Guía 8: 9 pruebas aprobadas.

Desde la raíz del repositorio:

```powershell
$env:PYTHONPATH = "cursada-uba-2025-2c/guias/guia-07/codigo"
python -m unittest discover -s cursada-uba-2025-2c/guias/guia-07/pruebas -p "*.py"
$env:PYTHONPATH = "cursada-uba-2025-2c/guias/guia-08/codigo"
python -m unittest discover -s cursada-uba-2025-2c/guias/guia-08/pruebas -p "*.py"
```

Los scripts históricos pueden pedir datos por consola al ejecutarse; por eso se documentan como ejercicios y no como módulos importables.

## Alcance y procedencia

La relación entre teoría, guías y código está documentada en [`docs/cursada-uba-2025-2c/mapa-teoria-ejercicios.md`](docs/cursada-uba-2025-2c/mapa-teoria-ejercicios.md). Los PDFs, planillas, reportes nominales, notebooks de otros cursos y material docente completo permanecen fuera de este repositorio hasta revisar licencias y procedencia.
