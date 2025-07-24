from app.config import INPUT_DATOS_BASICOS, OUTPUT_DATOS_BASICOS
from app.io_utils import cargar_datos, guardar_datos
from app.processor import limpiar_columnas, limpiar_num_documento, agregar_periodo_agrupado
from app.constants import COLUMNAS_A_BORRAR_DATOS_BASICOS
import pandas as pd

def reglas_datosbasicos():
    try:
        df = cargar_datos(INPUT_DATOS_BASICOS)
        print(f"✅ Archivo cargado en {INPUT_DATOS_BASICOS}")
    except FileNotFoundError as e:
         print(f"❌ Archivo de entrada no encontrado: {e}")
         return

    df = limpiar_columnas(df, columnas_a_borrar=COLUMNAS_A_BORRAR_DATOS_BASICOS, filas_a_borrar=2)
    df = limpiar_num_documento(df)
    df = agregar_periodo_agrupado(df)
    guardar_datos(df, OUTPUT_DATOS_BASICOS)
    print("\n| {:<40} | {:<10} |".format("Columna", "Tipo"))
    print("|" + "-" * 42 + "|" + "-" * 12 + "|")
    for col, dtype in df.dtypes.items():
        print("| {:<40} | {:<10} |".format(col, str(dtype)))