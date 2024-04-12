import streamlit as st


def file_uploader():
    if "planilha" not in st.session_state:
        planilha = st.file_uploader("Planilha", type=["xlsx"])

        if planilha:
            st.session_state.planilha = planilha
