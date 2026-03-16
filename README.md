# Reto Mundial 2026 - Aplicación DS

En este reto queremos identificar cuál será el equipo con mayor probabilidad de ganar el Mundial 2026. Además, puntos extra por:
- ¿Qué variable es más importante para ganarlo?
- ¿Qué confederación tiene más potencial de ser campeón?

## Columnas
Column	|Type	|Source
fifa_ranking_jan2026	|int	|Official FIFA — Jan 19, 2026
fifa_points_jan2026	|int	|Official FIFA — Jan 19, 2026
world_cup_titles	|int	|Historical fact
world_cup_finals	|int	|Historical fact
world_cup_appearances	|int	|Historical fact
star_player_rating	|float (0-10)	|Expert estimation
avg_player_age	|float	|Squad analysis
goalkeeper_rating	|float (0-10)	|Expert estimation
squad_depth_score	|float (0-10)	|Expert estimation
coach_experience_tournaments	|int	|Expert estimation
h2h_vs_top10_winrate	|float (0-1)	|Historical estimation
knockout_stage_reach_rate	|float (0-1)	|Historical WC data
is_host	|int (0/1)	|Official — USA, Canada, Mexico
