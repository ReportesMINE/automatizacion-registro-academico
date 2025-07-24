# Historia Académica ETL

Proyecto ETL modular con Python, Docker, Makefile y CI/CD.

## Requisitos

- Python 3.11+
- Docker instalado
- make instalado

## Validar ruta PowerShell

Get-Location | Select-Object -ExpandProperty Path

## Comandos Makefile

- `make historia` — Ejecuta flujo historia académica
- `make datosbasicos` — Ejecuta flujo datos básicos
- `make conflictohorario` — Ejecuta flujo conflicto horario
- `make historia-debug` — Ejecuta flujo historia con debug
- `make datosbasicos-debug` — Ejecuta flujo datos básicos con debug
- `make conflictohorario-debug` — Ejecuta flujo conflicto horario con debug
- `make build` — Construye imagen Docker
- `make run-historia` — Ejecuta contenedor historia académica
- `make run-datosbasicos` — Ejecuta contenedor datos básicos
- `make run-conflictohorario` — Ejecuta contenedor conflicto horario
- `make run-menu` — Ejecuta menú interactivo
- `make clean` — Limpia archivos temporales
- `make test-actions` — Prueba CI/CD

## Docker directo

docker build -t registro_academico .

docker run --rm -v ${PWD}/data:/app/data -v ${PWD}/output:/app/output registro_academico --historiaacademica

docker run --rm -v ${PWD}/data:/app/data -v ${PWD}/output:/app/output registro_academico --datosbasicos

docker run --rm -v ${PWD}/data:/app/data -v ${PWD}/output:/app/output registro_academico --conflictohorario

docker run -it -v "${PWD}/data:/app/data" -v "${PWD}/output:/app/output" registro_academico

## CI/CD

Ver `.github/workflows/etl.yml`.
