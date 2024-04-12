import streamlit as st


def values():
    if "planilha" in st.session_state and "dataframe" in st.session_state:
        c1, c2, c3 = st.columns(3)
        st.session_state.salario = c1.number_input("Salário do Consultor")
        st.session_state.ajuda = c2.number_input("Ajuda de Custo")
        st.session_state.estorno = c3.number_input("Valor à ser Estornado")
