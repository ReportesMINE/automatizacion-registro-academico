# config.py
from pathlib import Path

# Raíz del proyecto (un nivel arriba de /app)
BASE_DIR = Path(__file__).resolve().parent.parent

# Carpetas base
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

# === Historia Académica ===
INPUT_HISTORIA_ACADEMICA = DATA_DIR / "20251303_Registro_HistoriaAcademica.xlsx"
OUTPUT_HISTORIA_ACADEMICA = OUTPUT_DIR / "20251303_Transformado_HistoriaAcademica.xlsx"

# === Datos Básicos ===
INPUT_DATOS_BASICOS = DATA_DIR / "20251303_Registro_HistoriaDatosBasicos.xlsx"
OUTPUT_DATOS_BASICOS = OUTPUT_DIR / "20251303_Transformado_HistoriaDatosBasicos.xlsx"

# === Conflicto Horario ===
INPUT_CONFLICTO_HORARIO = DATA_DIR / "20250528_Solicitudes_ConflictoHorario.xlsx"
OUTPUT_CONFLICTO_HORARIO = OUTPUT_DIR / "20250528_Transformado_ConflictoHorario.xlsx"
