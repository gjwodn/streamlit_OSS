import streamlit as st

x = st.slider('컴퓨터소프트웨어학부 허재우')

OSS_score = [80,75,80,91,70,85]

st.line_chart(OSS_score)