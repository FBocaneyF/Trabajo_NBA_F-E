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
    df = df[df['SEASON'] >= 2018]

    return df

df_nba = cargar_y_limpiar_datos()



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

 # nombres de categorías correspondientes a condición
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


# PRIMERO, la bienvenida y algunos datos.

def page_inicio (df_filtrada):
    """Inicio"""
    col1, col2=  st.columns ([6,3])

    with col1: 
        st.title("Bienvenido a estadísticas de la NBA!")
        st.markdown (" Este espacio explora los indicadores clave de rendimiento y el resultado final. ")
    with col2: st.image("data:image/png;base64,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")
    st.divider()

    st.subheader("Totales de la temporada")
    ti1, ti2, ti3, ti4= st.columns(4)
    ti1.metric("Puntos", f"{df_filtrada['PTS_home'].sum() + df_filtrada['PTS_away'].sum():,.0f}")
    ti2.metric("Rebotes", f"{df_filtrada['REB_home'].sum() + df_filtrada['REB_away'].sum():,.0f}")
    ti3.metric("Asistencias", f"{df_filtrada['AST_home'].sum() + df_filtrada['AST_away'].sum():,.0f}")
    ti4.metric("Partidos", f"{len(df_filtrada)}")
    st.info("Desde el menú de opciones seleccione su siguiente perspectiva")

#segundo un grafico que muestre la ccantidad a traves de los años
def page_volumen (df_filtrada):
    st.title("Métricas por temporada")
    st.markdown("Análisis de metricas anuales y si se han visto afectadas")

    df_nba['puntos_total'] = df_filtrada['PTS_home'] + df_filtrada['PTS_away']
    df_nba['ast_total'] = df_filtrada['REB_home'] + df_filtrada['REB_away']
    df_nba['reb_total'] = df_filtrada['AST_home'] + df_filtrada['AST_away']
    
    # Grafico
    evolucion = df_nba.groupby('SEASON')[['puntos_total', 'ast_total', 'reb_total']].sum().reset_index()
    
    # Gráfico de área con los tres
    # 2. Aseguramos que SEASON sea tratado como texto o entero para evitar el "2,008"
    evolucion['SEASON'] = evolucion['SEASON'].astype(str)

# 3. Crear el gráfico con Plotly
    fig = px.area(
    evolucion, 
    x='SEASON', 
    y=['puntos_total', 'ast_total', 'reb_total'],
    title="🏀 Evolución Histórica",
    labels={'value': 'Total Acumulado', 'SEASON': 'Temporada', 'variable': 'Métrica'},
    color_discrete_map={
        'puntos_total': '#FF007F',  
        'ast_total': '#FF66B2',    
        'reb_total': "#FFB3D9"      
    }
)


    fig.update_layout(
    font_family="Arial",
    title_font_size=22,
    hovermode="x unified",  
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

    fig.update_layout(barmode='overlay') 
    fig.update_traces(stackgroup=None)
    fig.update_xaxes(showgrid=False, type='category') 
    fig.update_yaxes(gridcolor='#EEE')

    st.plotly_chart(fig, use_container_width=True)

#tercera parte sobre los porcentajes de tiro
def page_FG(df_filtrada):
    st.title("🎯 Eficiencia vs Volatilidad")
    st.markdown("Análisis de la Ineficiencia vs Volatilidad en Derrotas")
    #pt1
    df_filtrada['FG_PCT_Perdedor'] = np.where(df_filtrada['HOME_TEAM_WINS'] == 0, 
                                  df_filtrada['FG_PCT_home'], 
                                  df_filtrada['FG_PCT_away'])

    df_filtrada['FG3_PCT_Perdedor'] = np.where(df_filtrada['HOME_TEAM_WINS'] == 0, 
                                   df_filtrada['FG3_PCT_home'], 
                                   df_filtrada['FG3_PCT_away'])

    df_filtrada['FT_PCT_Perdedor'] = np.where(df_filtrada['HOME_TEAM_WINS'] == 0, 
                                  df_filtrada['FT_PCT_home'], 
                                  df_filtrada['FT_PCT_away'])
    media_perdidas = df_filtrada['FG_PCT_Perdedor'].mean()
    desviacion_perdidas = df_filtrada['FG_PCT_Perdedor'].std()
    # CV
    volatilidad = (desviacion_perdidas / media_perdidas) * 100

    col1, col2 = st.columns(2)
    col1.metric("Eficiencia Media (FG%)", f"{media_perdidas:.2%}")
    col2.metric("Índice de Volatilidad", f"{volatilidad:.2f}%")

    st.subheader("Este análisis identifica si las derrotas son constantes o por picos de rendimiento.")
    st.divider()

    # grafico
    df_plot = df_filtrada[['FG_PCT_Perdedor', 'FG3_PCT_Perdedor', 'FT_PCT_Perdedor']].melt(
    var_name='Tipo de Tiro', 
    value_name='Porcentaje'
     )

# Cambio nombre
    nombres = {
    'FG_PCT_Perdedor': 'Campo (FG%)',
    'FG3_PCT_Perdedor': 'Triples (FG3%)',
    'FT_PCT_Perdedor': 'Libres (FT%)'
    }

    df_plot['Tipo de Tiro'] = df_plot['Tipo de Tiro'].map(nombres)


    paleta_rosa_neon = ['#FF007F', '#FF66B2', '#FFB3D9'] 

    fig = px.box(
    df_plot, 
    x="Tipo de Tiro", 
    y="Porcentaje", 
    color="Tipo de Tiro",
    title="Análisis de Eficiencia en Derrotas",
    labels={'Porcentaje': 'Efectividad (%)'},
    color_discrete_sequence=paleta_rosa_neon,
    points="outliers",           
    hover_data={'Porcentaje': ':.1%'} 
    )

    fig.update_layout(
    template="plotly_dark",
    font_family="Roboto, Arial", 
    title_font_size=24,
    showlegend=False,
    xaxis=dict(
        showgrid=False,
        title_font_size=18,
        tickfont_size=16
    ),
    yaxis=dict(
        tickformat='.0%', 
        gridcolor='#444444', 
        zeroline=False,
        range=[0, 1.0], 
        title_font_size=18,
        tickfont_size=14
    ),
    height=600,
    margin=dict(l=50, r=50, t=80, b=50), 
    paper_bgcolor='rgba(15, 15, 15, 0.9)', 
    plot_bgcolor='rgba(10, 10, 10, 0)'
)
    #referencia en el 50% 
    fig.add_hline(y=0.50, line_dash="dot", line_color="#888888", opacity=0.5)

    st.plotly_chart(fig, use_container_width=True)

def page_reb(df_filtrada):
    st.title("🛡️ Dominio del Rebote")
    st.markdown("Análisis de los rebotes y puentos anotados")

    col1, col2, col3 = st.columns(3)
    col1.metric("Promedio Rebotes Ganador", f"{avg_ganador:.1f}")
    col2.metric("Promedio Rebotes Perdedor", f"{avg_perdedor:.1f}")
    col3.metric("% Victorias con +Rebotes", f"{porcentaje_exito:.1f}%")

    st.divider()
    st.subheader("Correlación: Rebotes vs. Puntos Anotados")
    fig_scatter = px.scatter(
    df_nba, 
    x='Diferencial_Rebotes', 
    y='Margen_Victoria',
    color='Margen_Victoria',  
    color_continuous_scale=['#333333', '#FF007B'], # De gris oscuro a naranja brillante
    trendline="ols", # Línea de Regresión Lineal (Mínimos Cuadrados)
    trendline_color_override="#FFFFFF", # Línea blanca para que resalte
    title="🏀 Impacto de los Rebotes en el Marcador Final",
    labels={
        'Diferencial_Rebotes': 'Ventaja en Rebotes', 
        'Margen_Victoria': 'Margen de Victoria (PTS)'
    },
    opacity=0.7,
    hover_data=['SEASON'] 
)

    fig_scatter.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="white",
    title_font_size=24,
    xaxis=dict(showgrid=False, zeroline=False),
    yaxis=dict(showgrid=True, gridcolor='#444444', zeroline=False),
    coloraxis_showscale=False # Ocultamos la barra de color para un look más limpio
    )

    fig_scatter.add_vline(x=0, line_dash="dot", line_color="#888888", line_width=1)
    fig_scatter.add_hline(y=0, line_dash="dot", line_color="#888888", line_width=1)

    fig_scatter.add_annotation(x=15, y=20, text="Dominio Total", showarrow=False, font_color="#FF4B00")
    fig_scatter.add_annotation(x=-15, y=-20, text="Déficit", showarrow=False, font_color="#888888")

    st.plotly_chart(fig_scatter, use_container_width=True)


#~ ~ ~ ~ ~ ~
#(NAVEGACION)
#~ ~ ~ ~ ~ ~

def main():
    
      st.sidebar.title("🏀 NBA Navigation")
      st.sidebar.markdown("Escoger...")

      #LISTA
      pages = {
          "🗑️Home": page_inicio,
          "📊Métricas por temporada": page_volumen,
          "🎯 Eficiencia vs Volatilidad": page_FG,
          "🛡️ Dominio del Rebote": page_reb
          }

      #MENU
      selection = st.sidebar.radio("Ir a:", list(pages.keys()))

      Tipo_selecionado= st.sidebar.multiselect(
          "Seleccione un tipo de juego",
          options=['Cerrado','Normal','Abierto'],
          default=['Cerrado','Normal','Abierto'],
          )
      
      if Tipo_selecionado:
          df_filtrado= df_nba[df_nba['Tipo_Juego'].isin(Tipo_selecionado)]
      else:
          df_filtrado= df_nba
      

      pages[selection](df_filtrado)

if __name__ == "__main__":
    main()
