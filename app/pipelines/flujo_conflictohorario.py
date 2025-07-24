from app.config import INPUT_CONFLICTO_HORARIO, OUTPUT_CONFLICTO_HORARIO
from app.io_utils import cargar_datos, guardar_datos
from app.processor import limpiar_columnas

def reglas_conflictohorario():
    try:
        df = cargar_datos(INPUT_CONFLICTO_HORARIO)
        print(f"✅ Archivo cargado en {INPUT_CONFLICTO_HORARIO}")
    except FileNotFoundError as e:
        print(f"❌ Archivo de entrada no encontrado: {e}")
        return

    df = limpiar_columnas(df, columnas_a_borrar=None, filas_a_borrar=1)
    guardar_datos(df, OUTPUT_CONFLICTO_HORARIO)
    print("\n| {:<40} | {:<10} |".format("Columna", "Tipo"))
    print("|" + "-" * 42 + "|" + "-" * 12 + "|")
    for col, dtype in df.dtypes.items():
        print("| {:<40} | {:<10} |".format(col, str(dtype)))
