import streamlit as st
from textos import texto_analise

st.set_page_config(layout='wide')

st.title('Tech Challenge: Previsão e Insights de Preços do Petróleo')

tabs = st.tabs(['Introdução', 'Análise', 'Previsão'])


with tabs[0]:
    st.header('Introdução')
    st.markdown(texto_analise, unsafe_allow_html=True)

with tabs[1]:
    st.header('Relatorio PowerBI')
    #st.write('Texto sobre o petroleo')
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiNmRkNWE0NDEtNzU5NS00MjUyLWI1ZjAtNmI2NTYzYjNiNDU5IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9"
    #st.components.v1.iframe(power_bi_url, width=800, height=600)
    st.markdown(
    f"<div style='display: flex; justify-content: center;'><iframe src='{power_bi_url}' width='2000' height='1000' frameborder='0' allowFullScreen='true'></iframe></div>",
    unsafe_allow_html=True
)
with tabs[2]:
    st.header('Previsão')
    st.write('Texto sobre o petroleo')
