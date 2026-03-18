# Reto Mundial 2026 - Aplicación DS

En este reto queremos identificar cuál será el equipo con mayor probabilidad de ganar el Mundial 2026. Además, puntos extra por:
- ¿Qué variable es más importante para ganarlo?
- Tiempo de ejecución de todas las simulaciones.
- Buenas prácticas.
- Justificación de decisiones.

Antes de entrar en proceso se debe correr el archivo *playoffs.py* para deteminar los equipos faltantes en los grupos, esto generará un archivo que se usará.

## Datos disponibles

- Información completa de calificación de equipos.
- Grupos en los que se encuentra cada equipo.
- Programación de partidos.

## Etapas de reto

- Determinar los clasificados de los playoffs preclasificados.
- Identificar posiciones en los grupos.
- Simular de los clasificados en fases de grupos, la probabilidad de ganar el mundial de los 32 equipos. 

## Columnas Data Set Base
Column	Type	Source
| Column                       | Type         | Source                         |
|------------------------------|--------------|--------------------------------|
| fifa_ranking        | int          | Official FIFA    |
| fifa_points          | int          | Official FIFA    |
| world_cup_titles             | int          | Historical fact                |
| world_cup_finals             | int          | Historical fact                |
| world_cup_appearances        | int          | Historical fact                |
| star_player_rating           | float (0-10) | Expert estimation              |
| avg_player_age               | float        | Squad analysis                 |
| goalkeeper_rating            | float (0-10) | Expert estimation              |
| squad_depth_score            | float (0-10) | Expert estimation              |
| coach_experience_tournaments | int          | Expert estimation              |
| h2h_vs_top10_winrate         | float (0-1)  | Historical estimation          |
| knockout_stage_reach_rate    | float (0-1)  | Historical WC data             |
| is_host                      | int (0/1)    | Official — USA, Canada, Mexico |

## A tener en cuenta 

Luego de simular todos los partidos de la fase de grupos se debe tener el cálculo de los puntos y luego usar la función a continuación:

```python
def seleccionar_clasificados(df, posc_col, puntos_col, rank_col, grupo_col):
    # 1. Clasificados directos (Posición 1 y 2 de cada grupo)
    directos = df[df[posc_col] <= 2].copy()
    
    # 2. Selección de los 8 mejores terceros
    terceros = df[df[posc_col] == 3].copy()
    
    # Ordenamos por Puntos (descendente) y luego por Ranking FIFA (ascendente: menor es mejor)
    mejores_terceros = terceros.sort_values(
        by=[puntos_col, rank_col], 
        ascending=[False, True]
    ).head(8)
    
    # Unificamos la lista final
    clasificados = pd.concat([directos, mejores_terceros])
    
    return clasificados.sort_values(by=[grupo_col, posc_col])

```
Con esta función se crearán las llaves de enfrentamientos. 
