# --------------------LIBRERÍAS----------------------------#
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template

# --------------------CONFIGURACIÓN DE LA PÁGINA----------------------------#
st.set_page_config(
    page_title="Malta",
    page_icon="🚢",
    layout="wide", #centered, wire
    initial_sidebar_state="expanded" #auto, collapsed, expanded
)

logo = "https://cdn.1min30.com/wp-content/uploads/2018/02/Couleur-logo-Airbnb-500x281.jpg"

# --------------------SIDEBAR----------------------------#
st.sidebar.image(logo, width=180)
st.sidebar.title("Introducción")
st.sidebar.write("-------------")


# Agregar contenido en la barra lateral
st.sidebar.header('Servicios ')
st.sidebar.write('Ofrece servicios para analizar conjuntos de datos con el objetivo de identificar tendencias, patrones.')

st.sidebar.header('Precios ')
st.sidebar.write('Cuando se trata de precios y variables, especialmente en el contexto de análisis de datos o modelos de negocios, hay varias consideraciones importantes que pueden influir en cómo se establecen los precios y qué variables se tienen en cuenta.')

st.sidebar.header('Reseñas ')
st.sidebar.write('La visualización de esta red de interacciones puede proporcionar una comprensión más profunda de cómo los usuarios interactúan entre sí en la plataforma de Airbnb. Por ejemplo, podría revelar patrones de comportamiento, como qué huéspedes suelen dejar revisiones positivas en los perfiles de ciertos anfitriones, o qué anfitriones reciben más interacciones por parte de diferentes huéspedes..')

# --------------------TABS----------------------------#
tab1, tab2, tab3 = st.tabs(
        ["Introducción", "desarrollo", "conclucíon"]
    )

# --------------------HEADER----------------------------#
# Ruta de la imagen en tu sistema de archivos
ruta_imagen = "https://www.mta.com.mt/en/file.aspx?f=29148"
# Mostrar la imagen en la aplicación
st.image(ruta_imagen, caption='Malta', use_column_width=True)

# primer grafico power bi
# Por ejemplo, gráficos, tablas, etc.

import streamlit as st

# segundo grafico power bi

st.title("Análisis de Datos")

def main():
    # Código HTML generado por Power BI 2222
    power_bi_html = """
    <iframe title="data_listings_graficos_2" width="550" height="900" src="https://app.powerbi.com/view?r=eyJrIjoiYWY1OWM5NDUtYWFlMy00Yzg5LWE1MTQtNjBlOWM4NDMyMTJjIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>"""
    
    # Insertar el código HTML en la aplicación Streamlit
    st.components.v1.html(power_bi_html, height=1200)

if __name__ == "__main__":
    main()
    
# --------------------graficos 2 -------------------------------#


st.header("Conclusión del Análisis de Datos de Airbnb en Malta")
st.write("""
El análisis detallado de los datos de Airbnb en Malta revela una serie de tendencias y patrones significativos que ofrecen una visión valiosa del mercado de alquileres vacacionales en la isla. A través de la exploración de variables clave como la ubicación, el tipo de propiedad, los precios y las valoraciones de los huéspedes, se ha obtenido una comprensión más profunda de la dinámica del mercado y las preferencias de los viajeros.

En primer lugar, se observa que las zonas costeras, especialmente aquellas cercanas a destinos turísticos populares como La Valeta, Sliema y St. Julian's, son las más demandadas en términos de alojamiento de Airbnb. Esto sugiere una clara preferencia por la proximidad a las atracciones turísticas y las comodidades locales entre los viajeros que eligen Malta como destino vacacional.

Además, se ha identificado una diversidad de opciones de alojamiento en términos de tipo de propiedad, que van desde apartamentos y casas adosadas hasta villas de lujo y habitaciones compartidas. Esta variedad ofrece a los viajeros una amplia gama de opciones para adaptarse a sus necesidades y presupuestos individuales.

En cuanto a los precios, se observa una fluctuación estacional, con picos durante los meses de verano y descensos durante la temporada baja. Sin embargo, dentro de cada temporada, existen diferencias significativas de precios según la ubicación y el tipo de propiedad. Por ejemplo, las propiedades ubicadas en zonas exclusivas tienden a tener precios más altos, mientras que aquellas en áreas menos turísticas pueden ofrecer tarifas más asequibles.

Las valoraciones de los huéspedes también juegan un papel crucial en la elección del alojamiento, con una correlación clara entre la calidad del servicio ofrecido por el anfitrión y la satisfacción general del huésped. Esto subraya la importancia de mantener altos estándares de hospitalidad y atención al cliente para garantizar experiencias positivas para los huéspedes y fomentar la repetición de negocios y recomendaciones.

En resumen, el análisis de datos de Airbnb en Malta proporciona una visión detallada y perspicaz del mercado de alquileres vacacionales en la isla. Estas conclusiones pueden ser de gran utilidad para propietarios, gestores de propiedades y viajeros por igual, al ofrecer información valiosa para la toma de decisiones informadas y la planificación de viajes memorables en esta encantadora isla mediterránea.


""")
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Código HTML generado por Power BI
    power_bi_html = """
    <iframe title="data_listings_graficos_2" width="550" height="900" src="https://app.powerbi.com/view?r=eyJrIjoiYWY1OWM5NDUtYWFlMy00Yzg5LWE1MTQtNjBlOWM4NDMyMTJjIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>"""

    return render_template('index.html', power_bi_html=power_bi_html)

if __name__ == '__main__':
    app.run(debug=True)

