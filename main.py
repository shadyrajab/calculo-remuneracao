import pandas as pd
import streamlit as st

from components.export import export_button
from components.filters import filters
from components.multipliers import multipliers
from components.uploader import file_uploader
from components.values import values
from pdfhandler.generatepdf import build_pdf_file
from pdfhandler.signature import create_signature_paragraph
from pdfhandler.statement import create_statement_paragraph
from pdfhandler.table import create_multipliers_table
from session.state import load_session
from utils.handler import handler_dataframe, handler_receita, handler_remuneracoes
from utils.variables import DATA

st.set_page_config(layout="wide")


file_uploader()

load_session()
filters()

c1, c2 = st.columns(2)

with c1:
    multipliers()

    if "consultor" in st.session_state:
        dataframe = handler_dataframe(st.session_state.consultor)

        handler_receita(dataframe)
        remuneracoes = handler_remuneracoes(
            st.session_state.consultor, st.session_state.faixa, st.session_state.filtro
        )

        dfr = pd.DataFrame(remuneracoes)
        st.dataframe(dfr, hide_index=True)

        values()

        multipliers_table = create_multipliers_table(DATA)
        signature = create_signature_paragraph(st.session_state.consultor)
        statement = create_statement_paragraph()

        build_pdf_file(multipliers_table, statement, signature)

        export_button()


with c2:
    if "planilha" in st.session_state and "dataframe" in st.session_state:
        if "consultor" in st.session_state:
            dataframe = handler_dataframe(st.session_state.consultor)

            dataframe = dataframe[dataframe["CONSULTOR"] == st.session_state.consultor]
            st.markdown("##### Vendas:")
            st.markdown("####")
            st.dataframe(dataframe, hide_index=True)
