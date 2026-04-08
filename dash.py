#Dashboar
#cargo librerias
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

#titulo y eso
st.set_page_config(
    page_title="Estadisticas de NBA",
    page_icon="🏀",
    layout="wide"
)

# el cache y los datos
@st.cache_data
def cargar_y_limpiar_datos():
    df = pd.read_csv("NBA.csv")
    columnas_brr = ['GAME_DATE_EST', 'GAME_ID', 'GAME_STATUS_TEXT', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'TEAM_ID_home', 'TEAM_ID_away']
    df = df.drop(columns=columnas_brr)
    df = df[df['SEASON'] == 2022]

    return df

df_nba = cargar_y_limpiar_datos()


#pt1
df_nba['FG_PCT_Perdedor'] = np.where(df_nba['HOME_TEAM_WINS'] == 0, 
                                  df_nba['FG_PCT_home'], 
                                  df_nba['FG_PCT_away'])

df_nba['FG3_PCT_Perdedor'] = np.where(df_nba['HOME_TEAM_WINS'] == 0, 
                                   df_nba['FG3_PCT_home'], 
                                   df_nba['FG3_PCT_away'])

df_nba['FT_PCT_Perdedor'] = np.where(df_nba['HOME_TEAM_WINS'] == 0, 
                                  df_nba['FT_PCT_home'], 
                                  df_nba['FT_PCT_away'])

    #  Calculo
media_perdidas = df_nba['FG_PCT_Perdedor'].mean()
desviacion_perdidas = df_nba['FG_PCT_Perdedor'].std()

    # CV
volatilidad = (desviacion_perdidas / media_perdidas) * 100



    #pt2 defino ganadores y perdedores en los pts y rebotes
# REBOTES
df_nba['REB_Ganador'] = np.where(df_nba['HOME_TEAM_WINS'] == 1, df_nba['REB_home'], df_nba['REB_away'])
df_nba['REB_Perdedor'] = np.where(df_nba['HOME_TEAM_WINS'] == 1, df_nba['REB_away'], df_nba['REB_home'])

# PUNTOS
df_nba['PTS_Ganador'] = np.where(df_nba['HOME_TEAM_WINS'] == 1, df_nba['PTS_home'], df_nba['PTS_away'])
df_nba['PTS_Perdedor'] = np.where(df_nba['HOME_TEAM_WINS'] == 1, df_nba['PTS_away'], df_nba['PTS_home'])


    # Diff de Rebotes y pts (G - P)
df_nba['Diferencial_Rebotes'] = df_nba['REB_Ganador'] - df_nba['REB_Perdedor']
df_nba['Margen_Victoria'] = df_nba['PTS_Ganador'] - df_nba['PTS_Perdedor']

    
avg_ganador = df_nba['REB_Ganador'].mean()
avg_perdedor = df_nba['REB_Perdedor'].mean()
partidos_mas_rebotes_ganan  = len(df_nba[df_nba['Diferencial_Rebotes'] > 0])
porcentaje_exito = (partidos_mas_rebotes_ganan / len(df_nba)) * 100


#pt3 definir las clasificaciones
# condiciones lógicas 
condiciones = [
    (df_nba['Margen_Victoria'] <= 5),
    (df_nba['Margen_Victoria'] > 5) & (df_nba['Margen_Victoria'] < 15),
    (df_nba['Margen_Victoria'] >= 15)
]

# nombres de categorias correspondientes a condicion
categorias = ['Cerrado', 'Normal', 'Abierto']

#  la nueva columna 
df_nba['Tipo_Juego'] = np.select(condiciones, categorias, default='Sin clasificar')

#ASISTENCIA
df_nba['AST_Ganador'] = np.where(df_nba['HOME_TEAM_WINS'] == 1, df_nba['AST_home'], df_nba['AST_away'])
df_nba['AST_Perdedor'] = np.where(df_nba['HOME_TEAM_WINS'] == 1, df_nba['AST_away'], df_nba['AST_home'])

df_nba['Diferencial_Asistencias'] = df_nba['AST_Ganador'] - df_nba['AST_Perdedor']

#FG ganador

df_nba['FG_PCT_Ganador'] = np.where(df_nba['HOME_TEAM_WINS'] == 1, 
                                  df_nba['FG_PCT_home'], 
                                  df_nba['FG_PCT_away'])




#titulo 
st.title("Dashboard de la NBA 🏀")
st.markdown('Anslisis de la temporada 2022 de partidos de la NBA')

#ventanita

tab1, tab2, tab3 = st.tabs([
    "🎯 Eficiencia vs Volatilidad", 
    "🛡️ Dominio del Rebote", 
    "📈 Competitividad y Estabilidad"
])

# OO 1
with tab1:
    st.header("Objetivo 1: Ineficiencia vs Volatilidad en Derrotas")


    st.header("Análisis de Derrotas (NBA 2022)")

    col1, col2, col3 = st.columns(3)
    col1.metric("Eficiencia Media (FG%)", f"{media_perdidas:.2%}")
    col2.metric("Índice de Volatilidad", f"{volatilidad:.2f}%")

    st.subheader("Este análisis identifica si las derrotas son constantes o por picos de rendimiento.")
    st.divider()

    # grafico
    df_plot = df_nba[['FG_PCT_Perdedor', 'FG3_PCT_Perdedor', 'FT_PCT_Perdedor']].melt(
        var_name='Tipo de Tiro', 
        value_name='Porcentaje'
    )
    
    # Cambio nombre
    nombres = {
        'FG_PCT_Perdedor': 'Tiro de Campo (FG%)',
        'FG3_PCT_Perdedor': 'Triples (FG3%)',
        'FT_PCT_Perdedor': 'Tiros Libres (FT%)'
    }
    df_plot['Tipo de Tiro'] = df_plot['Tipo de Tiro'].map(nombres)

    #  Boxplot 
    fig = px.box(
        df_plot, 
        x="Tipo de Tiro", 
        y="Porcentaje", 
        color="Tipo de Tiro",
        title="Comparación de Eficiencia y Volatilidad en Derrotas",
        labels={'Porcentaje': 'Efectividad (0.0 a 1.0)'},
        color_discrete_sequence=['#B05B77', '#D48197', '#EABDC8']
    )

    fig.update_layout(
        template="plotly_dark",
        yaxis_tickformat='.0%',
        showlegend=False,
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

    # la conclu
    st.markdown("""
    ### Interpretacion:
    * **Ineficiencia:** Si la "caja" de una métrica está muy abajo en el eje Y, esa es la principal deficiencia del equipo al perder.
    * **Volatilidad:** Mientras más larga sea la caja y los "bigotes", mayor es la inestabilidad en ese tipo de tiro. 
    * **Outliers (Puntitos aislados):** Son partidos donde el equipo tiró excepcionalmente bien (o mal) pero el resultado no cambió.
    """)


# OO 2

with tab2:
    st.header("Objetivo 2: Incidencia del Rebote en la Victoria")
    st.write("Comparacion los rebotes de ganadores vs perdedores.")
  
    col1, col2, col3 = st.columns(3)
    col1.metric("Promedio Rebotes Ganador", f"{avg_ganador:.1f}")
    col2.metric("Promedio Rebotes Perdedor", f"{avg_perdedor:.1f}")
    col3.metric("% Victorias con +Rebotes", f"{porcentaje_exito:.1f}%")

    st.divider()
    st.subheader("📈 Correlación: Rebotes vs. Puntos Anotados")

    fig_scatter = px.scatter(
        df_nba, x='Diferencial_Rebotes', y='Margen_Victoria',
        color_discrete_sequence=["#E87518"],
        title="Relación: Ventaja en Rebotes vs. Ventaja en Puntos",
        labels={'Diferencial_Rebotes': 'Diferencia de Rebotes', 
                'Margen_Victoria': 'Diferencia de Puntos'},
        opacity=0.6
    )
    # linea de tendencia para mostrar la incidencia
    fig_scatter.add_vline(x=0, line_dash="dash", line_color="gray")
    fig_scatter.add_hline(y=0, line_dash="dash", line_color="gray")
    
    st.plotly_chart(fig_scatter)

    # metricas de resumen
    correlacion = df_nba['Diferencial_Rebotes'].corr(df_nba['Margen_Victoria'])

    st.metric("Coeficiente de Correlación (Incidencia)", f"{correlacion:.2f}")
    
    st.write("""
    **Interpretación:** Un valor cercano a 1 indica que el dominio del rebote 
    está fuertemente asociado con un mayor margen de puntos en el marcador final.
    """)

    


# OO 3
with tab3:
    st.header("Objetivo 3: Margen de Victoria y Estabilidad")
    st.write("Análisis de juegos cerrados, normales y abiertos")
    
    pcts = df_nba['Tipo_Juego'].value_counts(normalize=True) * 100
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Cerrados", f"{pcts.get('Cerrado', 0):.1f}%")
    col2.metric("Normales", f"{pcts.get('Normal', 0):.1f}%")
    col3.metric("Abiertos", f"{pcts.get('Abierto', 0):.1f}%")
    
    st.divider() 

    fig = px.scatter(
        df_nba, 
        x="Diferencial_Asistencias",         
        y="Diferencial_Rebotes",          
        color="Tipo_Juego",
        size="FG_PCT_Ganador",         
        marginal_x="violin", 
        marginal_y="violin", 
        title="Relación Asistencias vs. Rebotes y su impacto en FG%",
        labels={"Diferencial_Asistencias": "Asistencias", "Diferencial_Rebotes": "Rebotes", "Tipo_Juego": "Competitividad"},
        color_discrete_map={
          "Cerrado": "#1B116A", 
          "Normal": "#255DB1",   
          "Abierto": "#5CB6FB",  
        },
        size_max=15,
        opacity=0.7,
    template="plotly_white",
    hover_data=["Margen_Victoria"] 
    )

    st.plotly_chart(fig, use_container_width=True, theme="streamlit", key="grafico_nba_objetivo3")

    st.write("""
    **Interpretación:** ,,,,
    """)
