import streamlit as st



def get_account_data():
    c1, c2, c3 = st.columns(3)

    st.session_state.agencia = c1.text_input("Agência")
    st.session_state.conta = c2.text_input("Conta")
    st.session_state.tipo_conta = c3.text_input("Tipo")