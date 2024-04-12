import streamlit as st


def filters():
    if "planilha" in st.session_state and "dataframe" in st.session_state:
        m1, m2, m3 = st.columns(3)
        st.session_state.consultor = m1.selectbox(
            "Selecionar Consultor",
            options=st.session_state.dataframe["CONSULTOR"].unique().tolist(),
        )

        df = st.session_state.dataframe[
            st.session_state.dataframe["CONSULTOR"] == st.session_state.consultor
        ]

        st.session_state.tipo = m2.multiselect(
            "Selecionar Tipo",
            options=df["TIPO VENDA"].unique().tolist(),
            default=df["TIPO VENDA"].unique().tolist(),
        )

        st.session_state.status = m3.multiselect(
            "Selecionar Status",
            options=df["STATUS"].unique().tolist(),
            default=df["STATUS"].unique().tolist(),
        )
