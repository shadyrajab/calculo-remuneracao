import streamlit as st


def filters():
    if "planilha" in st.session_state and "dataframe" in st.session_state:
        m1, m2, m3 = st.columns(3)
        st.session_state.consultor = m1.selectbox(
            "Selecionar Consultor",
            options=st.session_state.dataframe["CONSULTOR"].unique().tolist(),
        )
        st.session_state.salario = m2.number_input("Salário do Consultor")
        st.session_state.ajuda = m3.number_input("Ajuda de custo")

        st.markdown("##### Multiplicadores:")
        
        c1, c2, c3, c4, c5, c6 = st.columns(6)
        st.session_state.xnovos = c1.number_input("Novos", step=0.1)
        st.session_state.xportabilidade = c2.number_input("Portabilidade", step=0.1)
        st.session_state.xja_cliente = c3.number_input("Já Cliente", step=0.1)
        st.session_state.xmigracao_pre_pos = c4.number_input(
            "Migração Pré-Pós", step=0.1
        )
        st.session_state.xfixa = c5.number_input("Fixa", step=0.1)
        st.session_state.xavancada = c6.number_input("Avançada", step=0.1)
