from os.path import isfile

import pandas as pd
import streamlit as st


def file_uploader():
    planilha = True
    if not isfile("dataframe/movel.xlsx") and not isfile("dataframe/fixa.xlsx"):

        planilha = st.file_uploader("Planilha", type=["xlsx"])
        if planilha:
            movel = pd.read_excel(planilha, index_col=[0], sheet_name="MOVEL")
            fixa = pd.read_excel(planilha, index_col=[0], sheet_name="FIXA_E_AVANÇADA")

            movel.to_excel("dataframe/movel.xlsx", sheet_name="MOVEL")
            fixa.to_excel("dataframe/fixa.xlsx", sheet_name="FIXA_E_AVANÇADA")
