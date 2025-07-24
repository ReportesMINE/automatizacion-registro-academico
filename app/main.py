import argparse
import warnings

from app.pipelines.flujo_historiaacademica import reglas_historiaacademica
from app.pipelines.flujo_historiadatosbasicos import reglas_datosbasicos
from app.pipelines.flujo_conflictohorario import reglas_conflictohorario

warnings.filterwarnings("ignore", category=UserWarning)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Procesador ETL académico")
    parser.add_argument("--historiaacademica", action="store_true", help="Procesar Historia Académica")
    parser.add_argument("--datosbasicos", action="store_true", help="Procesar Historia Datos Básicos")
    parser.add_argument("--conflictohorario", action="store_true", help="Procesar Conflicto Horario")
    parser.add_argument("--todo", action="store_true", help="Procesar TODO")
    parser.add_argument("--debug", action="store_true", help="Modo debug")
    args = parser.parse_args()

    if args.debug:
        print("📌 Modo debug activado: {args}")

    if args.historiaacademica:
        print("⚙⚙ Ejecutando flujo Historia Académica...")
        reglas_historiaacademica()
    elif args.datosbasicos:
        print("⚙⚙ Ejecutando flujo Historia Datos Básicos...")
        reglas_datosbasicos()
    elif args.conflictohorario:
        print("⚙⚙ Ejecutando flujo Historia Datos Básicos...")
        reglas_conflictohorario()
    elif args.todo:
        print("⚙⚙ Ejecutando TODOS los flujos...")
        reglas_historiaacademica()
        reglas_datosbasicos()
        reglas_conflictohorario()
    else:
        print("⚠️ No se seleccionó ninguna opción")
