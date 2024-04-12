import streamlit as st


def file_uploader():
    planilha = st.file_uploader("Planilha", type=["xlsx"])

    if planilha:
        st.session_state.planilha = planilha
