import pandas as pd
import streamlit as st

from components.export import export_button
from components.filters import filters
from components.uploader import file_uploader
from pdfhandler.generatepdf import build_pdf_file
from pdfhandler.signature import create_signature_paragraph
from pdfhandler.statement import create_statement_paragraph
from pdfhandler.table import create_multipliers_table
from session.state import load_session
from utils.handler import handler_dataframe, handler_receita, handler_remuneracoes
from utils.variables import DATA

file_uploader()
load_session()

filters()

if "consultor" in st.session_state:
    dataframe = handler_dataframe(st.session_state.consultor)

    handler_receita(dataframe)
    remuneracoes = handler_remuneracoes(
        st.session_state.consultor, st.session_state.faixa, st.session_state.filtro
    )

    dfr = pd.DataFrame(remuneracoes)
    st.dataframe(dfr)

    multipliers_table = create_multipliers_table(DATA)
    signature = create_signature_paragraph(st.session_state.consultor)
    statement = create_statement_paragraph()

    build_pdf_file(multipliers_table, statement, signature)
    export_button()
