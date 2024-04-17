import re

import pandas as pd
import streamlit as st

from utils.functions import get_filtro
from utils.variables import JA_CLIENTE, MIGRACAO_PRE_POS, NOVOS, PORTABILIDADE


def format_value(value):
    formated_value = re.sub(r"[^0-9.]", "", str(value))
    if not formated_value:
        return 0
    return formated_value


def handler_dataframe(consultor: str):
    if "dataframe" in st.session_state:
        DATAFRAME: pd.DataFrame = st.session_state.dataframe

        dataframe = DATAFRAME[DATAFRAME["CONSULTOR"] == consultor]

        dataframe = dataframe[dataframe["TIPO VENDA"].isin(st.session_state.tipo)]
        dataframe = dataframe[dataframe["STATUS"].isin(st.session_state.status)]

        dataframe["R$ ACUMULADO"] = dataframe["R$ ACUMULADO"].apply(
            lambda v: format_value(v)
        )
        dataframe["R$ ACUMULADO"] = dataframe["R$ ACUMULADO"].astype(float)

        faixa = dataframe["R$ ACUMULADO"].sum()
        filtro = get_filtro(faixa, st.session_state.tipo_multiplicador)

        st.session_state.faixa = faixa
        st.session_state.filtro = filtro

        return dataframe


def handler_receita(df: pd.DataFrame):
    if "dataframe" in st.session_state:
        st.session_state.receita_novos = df[df["TIPO VENDA"].isin(NOVOS)][
            "R$ ACUMULADO"
        ].sum()
        st.session_state.receita_portabilidade = df[
            df["TIPO VENDA"].isin(PORTABILIDADE)
        ]["R$ ACUMULADO"].sum()
        st.session_state.receita_jacliente = df[df["TIPO VENDA"].isin(JA_CLIENTE)][
            "R$ ACUMULADO"
        ].sum()
        st.session_state.receita_migracaopp = df[
            df["TIPO VENDA"].isin(MIGRACAO_PRE_POS)
        ]["R$ ACUMULADO"].sum()
        st.session_state.receita_avancada = df[df["TIPO VENDA"] == "AVANÇADA"][
            "R$ ACUMULADO"
        ].sum()
        st.session_state.receita_fixa = df[df["TIPO VENDA"] == "FIXA"][
            "R$ ACUMULADO"
        ].sum()


def handler_remuneracoes(consultor: str, faixa: float, filtro: str):
    if "dataframe" in st.session_state:
        remuneracoes = [
            {
                "CONSULTOR": consultor,
                "FAIXA": faixa,
                "FILTRO": filtro,
                "*NOVOS": st.session_state.xnovos,
                "*PORTABILIDADE": st.session_state.xportabilidade,
                "*JÁ CLIENTE": st.session_state.xja_cliente,
                "*MIGRAÇÃO PRÉ/PÓS": st.session_state.xmigracao_pre_pos,
                "*FIXA": st.session_state.xfixa,
                "*AVANÇADA": st.session_state.xavancada,
                "NOVOS": st.session_state.receita_novos,
                "PORTABILIDADE": st.session_state.receita_portabilidade,
                "JÁ CLIENTE": st.session_state.receita_jacliente,
                "MIGRAÇÃO PRÉ/PÓS": st.session_state.receita_migracaopp,
                "AVANÇADA": st.session_state.receita_avancada,
                "FIXA": st.session_state.receita_fixa,
                "R NOVOS": st.session_state.receita_novos * st.session_state.xnovos,
                "R PORTABILIDADE": st.session_state.receita_portabilidade
                * st.session_state.xportabilidade,
                "R JÁ CLIENTE": st.session_state.receita_jacliente
                * st.session_state.xja_cliente,
                "R MIGRAÇÃO PRÉ/PÓS": st.session_state.receita_migracaopp
                * st.session_state.xmigracao_pre_pos,
                "R AVANÇADA": st.session_state.receita_avancada
                * st.session_state.xavancada,
                "R FIXA": st.session_state.receita_fixa * st.session_state.xfixa,
            }
        ]

        soma_r = (
            remuneracoes[0]["R NOVOS"]
            + remuneracoes[0]["R PORTABILIDADE"]
            + remuneracoes[0]["R JÁ CLIENTE"]
            + remuneracoes[0]["R MIGRAÇÃO PRÉ/PÓS"]
            + remuneracoes[0]["R AVANÇADA"]
            + remuneracoes[0]["R FIXA"]
        )

        remuneracoes[0]["R TOTAL"] = soma_r

        return remuneracoes
