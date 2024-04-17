import streamlit as st



def get_account_data():
    c1, c2, c3, c4 = st.columns(4)

    st.session_state.agencia = c1.text_input("Agência")
    st.session_state.conta = c2.text_input("Conta")
    st.session_state.tipo_conta = c3.text_input("Tipo")
    st.session_state.observacao = c4.text_input("Observação")