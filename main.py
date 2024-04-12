import pandas as pd
import streamlit as st

from components.filters import filters
from components.uploader import file_uploader
from session.state import load_session
from utils.handler import handler_dataframe, handler_receita, handler_remuneracoes

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