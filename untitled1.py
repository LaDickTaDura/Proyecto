import streamlit as st
import pandas as pd
import numpy as np

st.title("Licenciamiento Institucional")
st.write("El Licenciamiento Institucional es un procedimiento obligatorio para todas las universidades del país")
         
         
         
n= st.slider("n", 5, 100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)

