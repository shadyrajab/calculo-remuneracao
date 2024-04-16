import streamlit as st


def multipliers():
    if "dataframe" in st.session_state:
        st.markdown("##### Multiplicadores:")

        c1, c2, c3, c4, c5, c6 = st.columns(6)
        st.session_state.xnovos = c1.number_input("Novos", step=0.1)
        st.session_state.xportabilidade = c2.number_input("Portabilidade", step=0.1)
        st.session_state.xja_cliente = c3.number_input("Já Cliente", step=0.1)
        st.session_state.xmigracao_pre_pos = c4.number_input("Migração PP", step=0.1)
        st.session_state.xfixa = c5.number_input("Fixa", step=0.1)
        st.session_state.xavancada = c6.number_input("Avançada", step=0.1)
