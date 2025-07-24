# ====================================================
# Makefile para Historia Académica ETL
# ====================================================
IMAGE_NAME = registro_academico

.PHONY: historia datosbasicos historia-debug datosbasicos-debug build run-historia run-datosbasicos run-todo run-menu clean test-actions

HOST_PWD = $(shell powershell -Command "Get-Location | Select-Object -ExpandProperty Path")

# ====================================================
# Makefile para Imagen Docker en Local
# ====================================================
historia:
	py -m app.main --historiaacademica

datosbasicos:
	py -m app.main --datosbasicos

conflictohorario:
	py -m app.main --conflictohorario

historia-debug:
	py -m app.main --historiaacademica --debug

datosbasicos-debug:
	py -m app.main --datosbasicos --debug

conflictohorario:
	py -m app.main --conflictohorario --debug
# ====================================================
# Makefile para Flujos en Docker
# ====================================================
build:
	docker build -t $(IMAGE_NAME) .

run-historia:
	docker run --rm -v "$(HOST_PWD)/data:/app/data" -v "$(HOST_PWD)/output:/app/output" $(IMAGE_NAME) --historiaacademica

run-datosbasicos:
	docker run --rm -v "$(HOST_PWD)/data:/app/data" -v "$(HOST_PWD)/output:/app/output" $(IMAGE_NAME) --datosbasicos

run-conflictohorario:
	docker run --rm -v "$(HOST_PWD)/data:/app/data" -v "$(HOST_PWD)/output:/app/output" $(IMAGE_NAME) --conflictohorario

run-todo:
	docker run --rm -v "$(HOST_PWD)/data:/app/data" -v "$(HOST_PWD)/output:/app/output" $(IMAGE_NAME) --todo

run-menu:
	docker run -it --rm -v "$(HOST_PWD)/data:/app/data" -v "$(HOST_PWD)/output:/app/output" $(IMAGE_NAME)

# ====================================================
# Makefile para Pruebas CI/CD
# ====================================================
test-actions:
	echo "Este comando se prueba vía CI/CD en .github/workflows/etl.yml"

# ====================================================
# Makefile para Limpiar
# ====================================================
clean:
	rm -rf __pycache__ .venv output/*.xlsx
	echo "🧹 Carpeta limpia!"
