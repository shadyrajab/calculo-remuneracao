import streamlit as st


def download_pdf(path: str):
    with open(path, "rb") as f:
        data = f.read()

    return data


def export_button():
    if "dataframe" in st.session_state:
        st.download_button(
            "Gerar PDF",
            download_pdf("remunerações.pdf"),
            file_name="remunerações.pdf",
            mime="application/pdf",
        )
