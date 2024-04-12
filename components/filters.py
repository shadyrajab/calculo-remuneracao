import streamlit as st


def filters():
    if "planilha" in st.session_state and "dataframe" in st.session_state:
        st.session_state.consultor = st.selectbox(
            "Selecionar Consultor",
            options=st.session_state.dataframe["CONSULTOR"].unique().tolist(),
        )
        st.session_state.xnovos = st.number_input(
            "Multiplicador Novos", step=0.1
        )
        st.session_state.xportabilidade = st.number_input(
            "Multiplicador Portabilidade", step=0.1
        )
        st.session_state.xja_cliente = st.number_input(
            "Multiplicador Já Cliente", step=0.1
        )
        st.session_state.xmigracao_pre_pos = st.number_input(
            "Multiplicador Migração Pré-Pós", step=0.1
        )
        st.session_state.xfixa = st.number_input(
            "Multiplicador Fixa", step=0.1
        )
        st.session_state.xavancada = st.number_input(
            "Multiplicador Avançada", step=0.1
        )
