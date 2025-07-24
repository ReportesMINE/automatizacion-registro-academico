# Validación de Esquemas

Cada ejecución de pipeline genera la documentación y esta debe ser actualizada acá si cambia.
La fuente es descargada desde el sistema de registro de la universidad.

## Conflicto Horario
Fuente Coordinación: ConflictoHorario.xlsx
Renombramiento: 20250528_Solicitudes_ConflictoHorario.xlsx 
Destino: 20250528_Transformado_ConflictoHorario.xlsx

| Columna                                  | Tipo       |
|------------------------------------------|------------|
| Periodo                                  | object     |
| ID solicitud                             | float64    |
| Ticket                                   | object     |
| Código est                               | float64    |
| Login est                                | object     |
| NRC                                      | float64    |
| Nivel materia                            | object     |
| Facultad curso                           | object     |
| Departamento curso                       | object     |
| Lista cruzada                            | object     |
| Materia                                  | object     |
| Código materia                           | object     |
| Secc                                     | float64    |
| Nombre corto sección                     | object     |
| Desc. estado principal                   | object     |
| Desc. subestado                          | object     |
| Fecha creación                           | datetime64[ns] |
| Nombres                                  | object     |
| Apellidos                                | object     |
| Programa principal                       | object     |
| Segundo programa                         | object     |
| Créditos acumulados                      | float64    |
| Tipo solicitud                           | object     |
| Motivo                                   | object     |
| Opciones                                 | object     |
| SSC                                      | float64    |
| Primer semestre                          | object     |
| Fecha último estado                      | datetime64[ns] |
| Alternativas                             | object     |
| Descripción                              | object     |
| Profesor(es)                             | object     |


## Datos Básicos
Fuente Coordinación: Datosbasicos.xlsx
Renombramiento: 20251303_Registro_HistoriaDatosBasicos.xlsx 
Destino: 20251303_Transformado_HistoriaDatosBasicos.xlsx

| Columna                                  | Tipo       |
|------------------------------------------|------------|
| Periodo                                  | object     |
| Código est                               | float64    |
| Nombres                                  | object     |
| Apellidos                                | object     |
| Tipo de documento                        | object     |
| Num documento                            | object     |
| Sexo                                     | object     |
| Nacionalidad                             | object     |
| Ciudad de nacimiento                     | object     |
| Fecha de nacimiento                      | datetime64[ns] |
| Estrato                                  | float64    |
| Dirección residencia                     | object     |
| Ciudad residencia                        | object     |
| Departamento residencia                  | object     |
| País residencia                          | object     |
| Teléfono residencia                      | object     |
| Celular                                  | float64    |
| Programa principal                       | object     |
| Periodo de catálogo programa principal   | float64    |
| Nivel programa principal                 | object     |
| Facultad programa principal              | object     |
| Departamento programa principal          | object     |
| Segundo programa                         | object     |
| Periodo de catálogo segundo programa     | float64    |
| Nivel segundo programa                   | object     |
| Facultad segundo programa                | object     |
| Departamento segundo programa            | object     |
| Énfasis                                  | object     |
| Opciones inscritas                       | float64    |
| Primer programa actual                   | object     |
| Segundo programa actual                  | object     |
| Tercer programa actual                   | float64    |
| Tipo admisión                            | object     |
| Tipo alumno                              | object     |
| Pago                                     | object     |
| Apoyos financieros                       | object     |
| Estado académico inicio                  | object     |
| Estado académico fin                     | object     |
| Sobrepaso académico                      | object     |
| Periodo sobrepaso académico              | float64    |
| Estado inscripción                       | object     |
| Puede extracreditarse                    | object     |
| Créditos inscritos                       | float64    |
| Núm cursos inscritos                     | float64    |
| Créditos retirados                       | float64    |
| Núm cursos retirados                     | float64    |
| Nivel historia académica                 | object     |
| Promedio móvil                           | float64    |
| Créditos pdo intentado institucional     | float64    |
| Créditos pdo aprobado institucional      | float64    |
| Créditos pdo pga institucional           | float64    |
| Promedio pdo institucional               | float64    |
| Créditos pdo aprobado transferencias     | float64    |
| Créditos pdo pga transferencias          | float64    |
| Promedio pdo transferencias              | float64    |
| Créditos pdo global                      | float64    |
| Promedio pdo global (PROM. SEM/PDO)      | float64    |
| Créditos acum aprobado transferencia     | float64    |
| Promedio acum transferencia              | float64    |
| Créditos intentado acum global           | float64    |
| Créditos aprobado acum global            | float64    |
| Créditos acum pga global                 | float64    |
| Promedio institucional acum              | float64    |
| Promedio global acum (PGA)               | float64    |
| SSC                                      | float64    |
| Puntos de calidad pdo                    | float64    |
| Puntos de calidad acumulado              | float64    |
| Candidato a grado                        | object     |
| Descripción estado de grado              | object     |
| Programa candidato a grado               | object     |
| Correo Uniandes                          | object     |
| Correo personal                          | object     |
| Periodo agrupado                         | object     |

## Historia Académica
Fuente Coordinación: HistoriaAcademica.xlsx
Renombramiento: 20251303_Registro_HistoriaAcademica.xlsx
Destino: 20251303_Transformado_HistoriaAcademica.xlsx

| Columna                                  | Tipo       |
|------------------------------------------|------------|
| Periodo                                  | object     |
| Materia/examen                           | object     |
| Nombre largo curso o examen              | object     |
| Código est                               | float64    |
| Nota final                               | float64    |
| Programa principal                       | object     |
| Nivel programa principal                 | object     |
| Curso abreviado                          | object     |