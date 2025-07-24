import pandas as pd
from typing import Optional
from app.constants import ABREVIACIONES, COLUMNAS_ORDENADAS

def limpiar_columnas(df: pd.DataFrame,columnas_a_borrar: Optional[list] = None,filas_a_borrar: int = 2) -> pd.DataFrame:
    if columnas_a_borrar:
        df.drop(columns=columnas_a_borrar, inplace=True, errors="ignore")
    if filas_a_borrar > 0:
        df = df.iloc[:-filas_a_borrar]
    return df

def abreviar_cursos(df: pd.DataFrame) -> pd.DataFrame:
    df["Curso abreviado"] = df["Nombre largo curso o examen"].map(ABREVIACIONES)
    df["Curso abreviado"] = df["Curso abreviado"].fillna(df["Nombre largo curso o examen"])
    return df

def limpiar_notas(df: pd.DataFrame) -> pd.DataFrame:
    df["Nota final"] = pd.to_numeric(df["Nota final"], errors="coerce")
    if "Kept Errors" in df.iloc[-1].values:
        df = df.iloc[:-1]
    return df

def reorganizar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    return df[COLUMNAS_ORDENADAS]

def limpiar_num_documento(df: pd.DataFrame) -> pd.DataFrame:
    #Limpia la columna 'Num documento' dejando solo números.
    df["Num documento"] = df["Num documento"].astype(str).str.strip()
    return df

def agregar_periodo_agrupado(df: pd.DataFrame) -> pd.DataFrame:
    #Agrega una columna 'Periodo agrupado' tomando los 4 primeros dígitos de la columna 'Periodo'.
    df["Periodo agrupado"] = df["Periodo"].astype(str).str[:4]
    return df