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

# el cacho y los datos
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


#titulo del pedazo blanco
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

    st.info("Este análisis identifica si las derrotas son constantes o por picos de rendimiento.")
    st.divider()

    # graficote
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
    st.markdown(
    ### Interpretacion:
    )

    
# OO 2

with tab2:
    st.header("Objetivo 2: Incidencia del Rebote en la Victoria")
    st.write("Comparacion los rebotes de ganadores vs perdedores.")


    
