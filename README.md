# Introducción


## Estructura del Informe
Este documento técnico se encuentra estructurado en cinco capítulos fundamentales:

**Capítulo I** Se expone la relevancia de analizar la consistencia deportiva frente a la efectividad aislada, formulando las preguntas de investigación y delimitando el alcance.

**Capítulo II** Establece el Marco Teórico, definiendo los conceptos estadísticos clave como, necesarios para la interpretación de los datos.

**Capítulo III** Describe el Marco Metodológico, detallando el proceso de limpieza de datos (ETL), las pruebas de hipótesis y los algoritmos utilizados para validar la calidad de la información.

**Capítulo IV** Presenta el Análisis de Resultados, donde se exhiben las tablas y gráficos generados dinámicamente.

**Capítulo V** Expone los hallazgos finales sobre qué factores determinaron la victoria en 2022. Se concluye sobre la estabilidad de los equipos y se ofrecen recomendaciones estratégicas basadas en la evidencia estadística obtenida.

# Planteamiento del Problema
 En el baloncesto de élite, ganar un partido no siempre depende de qué tan alto sea el promedio de un equipo, sino de qué tan **consistente** pueda ser ese rendimiento bajo presión. El análisis de los 542 registros de la NBA en 2022 revela una interrogante crítica: ¿se pierden los partidos por una falta de talento general o por una **irregularidad drástica** en momentos clave?
 
El problema radica en que el porcentaje de tiro (FG_PCT) suele ser volátil. Cuando un equipo pierde, no siempre queda claro si es por una ineficiencia constante o por una alta variabilidad (inestabilidad) en sus lanzamientos. Además, existe una brecha en la comprensión de cómo factores específicos, como superar el **50% de efectividad de campo** o dominar la **batalla de rebotes**, actúan como predictores determinantes de la victoria.

Debido a esto, se plantea las siguientes preguntas de investigación:

**1.** ¿Es la derrota en la NBA 2022 consecuencia de una ineficiencia constante en el tiro o se debe a una alta volatilidad e inestabilidad en el porcentaje de campo?

**2.** ¿Como incide la capacidad de domino en el rebote sobre la victoria en el marcador final?

**3.** ¿Existe una relación en la que los indicadores clave de rendimiento (puntos, rebotes y asistencias) afecten a la estabilidad en el tiro de campo, y si en los juegos más cerrados tienen un menor porcentaje?


## Justificación
El presente trabajo se delimita al análisis de la temporada 2022 con el fin de garantizar la homogeneidad en el contexto táctico y reglamentario de los datos. La selección de este periodo y de las variables correspondientes responde a los siguientes criterios:

Se priorizan aquellos indicadores que reflejan directamente la eficiencia ofensiva y el control del juego, permitiendo un análisis con mayor valor interpretativo.
 El uso de este subconjunto de datos facilita la aplicación de herramientas de tendencia central, dispersión y tablas bivariantes, objetivos principales de este estudio.
 
 Al centrarse en un año específico, se eliminan ruidos estadísticos provocados por la evolución histórica del juego, permitiendo conclusiones más precisas sobre el rendimiento contemporáneo en la NBA.

# Objetivos

## Objetivo General
Evaluar la incidencia de la estabilidad en el tiro y la relación entre indicadores clave de rendimiento en el resultado final de los partidos de la NBA en el año 2022.

## Objetivos Específicos

**1.** Describir el comportamiento del porcentaje de tiro de campo en los partidos perdidos para identificar si predominan niveles bajos de eficiencia o una mayor variabilidad en el rendimiento de tiro.

**2.** Explorar la asociación entre la cantidad de rebotes obtenidos y el resultado final de los partidos mediante herramientas de estadística descriptiva.

**3.** Clasificar los encuentros de la temporada 2022 de la NBA según su margen de competitividad (diferencia en el marcador) y comparar la estabilidad en el porcentaje de tiro de campo entre los distintos niveles de competitividad.

