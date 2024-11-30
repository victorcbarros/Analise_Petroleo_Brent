import streamlit as st
from textos import texto_analise

st.set_page_config(layout='wide')

st.title('Tech Challenge: Previsão e Insights de Preços do Petróleo')

tabs = st.tabs(['Introdução', 'Análise', 'Previsão'])


with tabs[0]:
    st.header('Introdução')
    st.markdown(texto_analise, unsafe_allow_html=True)

with tabs[1]:
    st.header('Análise')
    st.write('Texto sobre o petroleo')

with tabs[2]:
    st.header('Previsão')
    st.write('Texto sobre o petroleo')
