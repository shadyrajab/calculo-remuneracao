import streamlit as st

from utils.functions import get_multiplier
from utils.variables import CONSULTORES_MULTIPLICADOR_PADRAO


def multipliers():
    if "dataframe" in st.session_state:
        if st.session_state.consultor not in CONSULTORES_MULTIPLICADOR_PADRAO:
            values = get_multiplier("default")

        else:
            values = get_multiplier(st.session_state.filtro)

        c1, c2, c3, c4, c5, c6 = st.columns(6)
        st.session_state.xnovos = c1.number_input(
            "Novos", step=0.1, value=values["NOVOS"]
        )
        st.session_state.xportabilidade = c2.number_input(
            "Portabilidade", step=0.1, value=values["PORTABILIDADE"]
        )
        st.session_state.xja_cliente = c3.number_input(
            "Já Cliente", step=0.1, value=values["ALTAS"]
        )
        st.session_state.xmigracao_pre_pos = c4.number_input(
            "Migração PP", step=0.1, value=values["ALTAS"]
        )
        st.session_state.xfixa = c5.number_input("Fixa", step=0.1, value=values["FIXA"])
        st.session_state.xavancada = c6.number_input(
            "Avançada", step=0.1, value=values["AVANÇADA"]
        )
