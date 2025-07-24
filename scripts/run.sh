#!/bin/bash

if [ -z "$1" ]; then
  echo "=== Selecciona una opción ==="
  select opcion in "Historia Académica" "Datos Básicos" "Conflicto Horario" "Todos los Flujos" "Salir"; do
    case $REPLY in
      1) python -m app.main --historiaacademica ;;
      2) python -m app.main --datosbasicos ;;
      3) python -m app.main --conflictohorario ;;
      4) python -m app.main --todo ;;
      5) exit 0 ;;
    esac
    break
  done
else
  echo "🟢 Ejecutando con argumento directo: $1"
  python -m app.main "$@"
fi