from os.path import isfile

import pandas as pd
import streamlit as st

from utils.variables import CONCLUIDOS_FIXA, CONCLUIDOS_MOVEL


def load_session():
    if isfile("dataframe/movel.xlsx") and isfile("dataframe/fixa.xlsx"):
        if "movel" not in st.session_state and "fixa" not in st.session_state:

            # Ler e filtrar a planilha das vendas Móvel
            movel = pd.read_excel("dataframe/movel.xlsx", index_col=[0])

            movel.rename(columns={"QTD SERVIÇOS": "QUANTIDADE"}, inplace=True)
            st.session_state.movel = movel[
                [
                    "CONSULTOR",
                    "RAZÃO SOCIAL",
                    "STATUS",
                    "PLANO",
                    "VALOR DO PLANO",
                    "QUANTIDADE",
                    "R$ ACUMULADO",
                    "TIPO VENDA",
                ]
            ]

            # Ler, filtrar a tratar a planilha das vendas Fixa
            fixa = pd.read_excel("dataframe/fixa.xlsx", index_col=[0])

            # Criar coluna valor acumulado que não existe na planilha fixa, e adequar o nomes
            # das colunas para ficar padronizado.
            fixa["R$ ACUMULADO"] = fixa["QUANTIDADE"] * fixa["VALOR DO PLANO"]
            fixa.rename(columns={"TIPO DE VENDA": "TIPO VENDA"}, inplace=True)

            st.session_state.fixa = fixa[
                [
                    "CONSULTOR",
                    "RAZÃO SOCIAL",
                    "STATUS",
                    "PLANO",
                    "VALOR DO PLANO",
                    "QUANTIDADE",
                    "R$ ACUMULADO",
                    "TIPO VENDA",
                ]
            ]

        if (
            ("dataframe" not in st.session_state)
            and ("movel" in st.session_state)
            and ("fixa" in st.session_state)
        ):

            # Concatenar as planilhas FIXA e MÓVEL e armazenar na sessão
            dataframe = pd.concat([st.session_state.fixa, st.session_state.movel])
            dataframe.dropna(inplace=True)

            st.session_state.dataframe = dataframe[
                dataframe["STATUS"].isin(CONCLUIDOS_MOVEL + CONCLUIDOS_FIXA)
            ]
