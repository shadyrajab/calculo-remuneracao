import streamlit as st


def tipo_multiplicador():
    st.session_state.tipo_multiplicador = st.selectbox(
        "Tipo de Multiplicador", options=["Efetivo", "Estágio"]
    )
