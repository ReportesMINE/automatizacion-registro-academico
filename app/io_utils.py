import pandas as pd
from pathlib import Path

def cargar_datos(path: Path) -> pd.DataFrame:
    #Carga archivo Excel, reemplaza celdas vacías y borra filas vacías
    df = pd.read_excel(path)
    df.replace(r'^\s*$', pd.NA, regex=True, inplace=True)
    df.dropna(how="all", inplace=True)
    return df

def guardar_datos(df: pd.DataFrame, path: Path) -> None:
    #Guarda el DataFrame en Excel y muestra feedback
    path.parent.mkdir(parents=True, exist_ok=True)  # Crea carpeta si no existe
    print(f"💾 Guardando archivo en: {path}")
    df.to_excel(path, index=False)

