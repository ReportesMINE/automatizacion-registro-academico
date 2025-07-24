from app.config import INPUT_HISTORIA_ACADEMICA, OUTPUT_HISTORIA_ACADEMICA
from app.io_utils import cargar_datos, guardar_datos
from app.processor import limpiar_columnas, abreviar_cursos, limpiar_notas, reorganizar_columnas
from app.constants import COLUMNAS_A_BORRAR_HISTORIA_ACADEMICA

def reglas_historiaacademica():
    try:
        df = cargar_datos(INPUT_HISTORIA_ACADEMICA)
        print(f"✅ Archivo cargado en {INPUT_HISTORIA_ACADEMICA}")
    except FileNotFoundError as e:
        print(f"❌ Archivo de entrada no encontrado: {e}")
        return

    df = limpiar_columnas(df, columnas_a_borrar=COLUMNAS_A_BORRAR_HISTORIA_ACADEMICA, filas_a_borrar=2)
    df = abreviar_cursos(df)
    df = limpiar_notas(df)
    df = reorganizar_columnas(df)
    guardar_datos(df, OUTPUT_HISTORIA_ACADEMICA)
    print("\n| {:<40} | {:<10} |".format("Columna", "Tipo"))
    print("|" + "-" * 42 + "|" + "-" * 12 + "|")
    for col, dtype in df.dtypes.items():
        print("| {:<40} | {:<10} |".format(col, str(dtype)))
