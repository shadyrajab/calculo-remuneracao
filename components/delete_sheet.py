import os

import streamlit as st


def delete_sheet_button():
    button = st.button("Deletar")

    if button:
        os.remove("dataframe/fixa.xlsx")
        os.remove("dataframe/movel.xlsx")

        del st.session_state["consultor"]
        del st.session_state["dataframe"]
        del st.session_state["movel"]
        del st.session_state["fixa"]
