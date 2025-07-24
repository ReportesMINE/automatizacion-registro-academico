# Nombramiento y relaciones de tableros Power BI

Cuando se desee crear una nueva **vista** basada en el nombramiento de un tablero ya existente, y su nombre de **fuente de datos** ya esté en uso, 
se recomienda usar un **guion (-)** para especificar que se trata de un **detalle o variante** adicional de esa vista.  

---

# Rutas Online
Repositorio Ruta Fuente : https://uniandes.sharepoint.com/sites/MINE779/Documentos%20compartidos/General/Anal%C3%ADtica/Datos/Raw/

Repositorio Ruta Destino : https://uniandes.sharepoint.com/sites/MINE779/Documentos%20compartidos/General/Anal%C3%ADtica/Datos/Processed/

---

## Estructura

| Proyecto `.pbix`                  | Tablero                    | Fuente de datos (`Power Query Editor`)         |
|-----------------------------------|----------------------------|-----------------------------------------------|
| **HistoriaAcademica.pbix**        | HistoriaAcademica-General  | `20251303_Transformado_HistoriaAcademica`     |
|                                   | HistoriaAcademica-Cursos   | `20251303_Transformado_HistoriaAcademica`     |
|                                   | HistoriaAcademica-MINE     | `20251303_Transformado_HistoriaAcademica`     |
|                                   | HistoriaDatosBasicos       | `20251303_Transformado_HistoriaDatosBasicos`  |
| **ReportesConflictoHorario.pbix** | ConflictoHorario-Cursos    | `20250528_Transformado_ConflictoHorario`      |
|                                   | ConflictoHorario-Periodos  | `20250528_Transformado_ConflictoHorario`      |

---

## Buenas prácticas

- Usar nombres **claros y descriptivos** para los tableros.
- Mantener la **coherencia** entre nombre de tablero y archivo transformado.
- Agregar un **sufijo** con guion para distinguir variantes o detalles (`-Cursos`, `-General`, `-Periodos`, etc.).

---