import pandas as pd
import streamlit as st

from components.contas import get_account_data
from components.delete_sheet import delete_sheet_button
from components.export import export_button
from components.filters import filters
from components.multipliers import multipliers
from components.tipo_multiplicador import tipo_multiplicador
from components.uploader import file_uploader
from components.values import values
from pdfhandler.account import create_account_table
from pdfhandler.generatepdf import build_pdf_file
from pdfhandler.information import create_informatons_table
from pdfhandler.multipliers import create_multipliers_table
from pdfhandler.signature import create_signature_paragraph
from pdfhandler.statement import create_statement_paragraph
from session.state import load_session
from utils.functions import get_information_data, get_multipliers_data
from utils.handler import handler_dataframe, handler_receita, handler_remuneracoes

st.set_page_config(layout="wide")


file_uploader()

load_session()
filters()
st.markdown("##### Multiplicadores:")
tipo_multiplicador()
c1, c2 = st.columns(2)

with c1:
    if "consultor" in st.session_state:
        dataframe = handler_dataframe(st.session_state.consultor)
        multipliers()
        handler_receita(dataframe)
        remuneracoes = handler_remuneracoes(
            st.session_state.consultor, st.session_state.faixa, st.session_state.filtro
        )

        dfr = pd.DataFrame(remuneracoes)
        st.dataframe(dfr, hide_index=True)

        values()
        get_account_data()

        information_data = get_information_data(
            dfr["R TOTAL"][0],
            st.session_state.salario,
            st.session_state.ajuda,
            st.session_state.estorno,
            dfr["FAIXA"][0],
        )

        multipliers_data = get_multipliers_data(dfr)

        multipliers_table = create_multipliers_table(multipliers_data)
        signature = create_signature_paragraph(st.session_state.consultor)
        statement = create_statement_paragraph()
        informations = create_informatons_table(information_data)
        account = create_account_table(
            st.session_state.agencia,
            st.session_state.conta,
            st.session_state.tipo_conta,
        )
        build_pdf_file([multipliers_table, informations, account, statement, signature])
        b1, b2, b3, b4, b5, b6 = st.columns(6)
        with b1:
            export_button()

        with b2:
            delete_sheet_button()


with c2:
    if "dataframe" in st.session_state:
        if "consultor" in st.session_state:
            dataframe = handler_dataframe(st.session_state.consultor)

            dataframe = dataframe[dataframe["CONSULTOR"] == st.session_state.consultor]
            st.markdown("##### Vendas:")
            st.markdown("####")
            st.dataframe(dataframe, hide_index=True)
