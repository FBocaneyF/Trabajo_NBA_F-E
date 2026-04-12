# Introducción
 La NBA es la mejor liga de baloncesto del mundo, donde los mejores jugadores compiten constantemente bajo presión. En esta Competencia, ganar un partido no solo depende del talento físico, sino también de la inteligencia táctica y del manejo de los datos. El baloncesto moderno de hoy se apoya en la estadística para entender qué factores, como la puntería o el control de los rebotes, aseguran que un equipo permanezca en la cima.

 El presente estudio analiza el desempeño de los equipos de la NBA durante la temporada 2022, utilizando una base de datos de 542 partidos. El objetivo principal es entender por qué algunos equipos ganan y otros pierden, y si esto se debe a una falta de puntería constante o a rachas de inestabilidad durante el juego.

 A través de herramientas de estadística y computación, este trabajo explora cómo influyen el porcentaje de tiros, los rebotes y las asistencias en el marcador final. No se trata solo de ver quién anota más, sino de identificar qué factores, como el control del balón y la consistencia en los lanzamientos, son los que realmente aseguran la victoria.


## Estructura del Informe
Este documento técnico se encuentra estructurado en cinco capítulos fundamentales:

**Capítulo I** Se expone la relevancia de analizar la consistencia deportiva frente a la efectividad aislada, formulando las preguntas de investigación y delimitando el alcance.

**Capítulo II** Establece el Marco Teórico, definiendo los conceptos estadísticos clave como, necesarios para la interpretación de los datos.

**Capítulo III** Describe el Marco Metodológico, detallando el proceso de limpieza de datos (ETL), las pruebas de hipótesis y los algoritmos utilizados para validar la calidad de la información.

**Capítulo IV** Presenta el Análisis de Resultados, donde se exhiben las tablas y gráficos generados dinámicamente.

**Capítulo V** Expone los hallazgos finales sobre qué factores determinaron la victoria en 2022. Se concluye sobre la estabilidad de los equipos y se ofrecen recomendaciones estratégicas basadas en la evidencia estadística obtenida.

# Planteamiento del Problema
 En el baloncesto de élite, ganar un partido no siempre depende de qué tan alto sea el promedio de un equipo, sino de qué tan **consistente** pueda ser ese rendimiento bajo presión. El análisis de los 542 registros de la NBA en 2022 revela una interrogante crítica: ¿se pierden los partidos por una falta de talento general o por una **irregularidad drástica** en momentos clave?
 
El problema radica en que el porcentaje de tiro suele ser volátil. Cuando un equipo pierde, no siempre queda claro si es por una ineficiencia constante o por una alta variabilidad (inestabilidad) en sus lanzamientos. Además, existe una brecha en la comprensión de cómo factores específicos, como superar el **50% de efectividad de campo** o dominar la **batalla de rebotes**, actúan como predictores determinantes de la victoria.

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
Evaluar la incidencia de la estabilidad en el tiro y la relación de variables de efectividad y posesión en el resultado final de los partidos de la NBA en el año 2022, mediante el análisis de medidas de dispersión y tablas de contingencia.

## Objetivos Específicos

**1.** Describir el comportamiento del porcentaje de tiro de campo en los partidos perdidos para identificar si predominan niveles bajos de eficiencia o una mayor variabilidad en el rendimiento de tiro.

**2.** Explorar la asociación entre la cantidad de rebotes obtenidos y el resultado final de los partidos mediante herramientas de estadística descriptiva.


link:(ahorita lo arreglo mas bonita): https://trabajo-nba-f-e-97.onrender.com/

**3.** Clasificar los encuentros de la temporada 2022 de la NBA según su margen de competitividad en los indicadores clave de rendimiento y comparar la estabilidad en el porcentaje de tiro de campo entre los distintos niveles de competitividad.


