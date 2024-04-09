import pandas as pd
import streamlit as st

from faixas import MULTIPLICADORES, get_filtro

NOVOS = ["NOVO", "NOVO - VIVO TOTAL"]
PORTABILIDADE = [
    "PORTABILIDADE PF + TT PF/PJ",
    "PORTABILIDADE",
    "PORTABILIDADE - VIVO TOTAL",
    "PORTABILIDADE PF + TT PF/PJ - VIVO TOTAL",
    "PORTABILIDADE FWT",
]

JA_CLIENTE = ["JÁ CLIENTE"]
MIGRACAO_PRE_POS = ["MIGRAÇÃO PRÉ/PÓS", "MIGRAÇÃO PRÉ/PÓS - VIVO TOTAL"]
AVANCADA = ["AVANÇADA"]

CONCLUIDOS_MOVEL = ["CONCLUIDO", "FATURANDO-PORTABILIDADE"]
CONCLUIDOS_FIXA = ["ATIVO"]

planilha = st.file_uploader("Planilha", type=["xlsx"])

if planilha:
    if "movel" not in st.session_state:
        st.session_state.movel = pd.read_excel(
            planilha, index_col=[0], sheet_name="MOVEL"
        )
        st.session_state.movel = st.session_state.movel[
            ["CONSULTOR", "STATUS", "R$ ACUMULADO", "TIPO VENDA"]
        ]

    if "fixa" not in st.session_state:
        st.session_state.fixa = pd.read_excel(
            planilha, index_col=[0], sheet_name="FIXA_E_AVANÇADA"
        )
        st.session_state.fixa["R$ ACUMULADO"] = (
            st.session_state.fixa["QUANTIDADE"]
            * st.session_state.fixa["VALOR DO PLANO"]
        )
        st.session_state.fixa.rename(
            columns={"TIPO DE VENDA": "TIPO VENDA"}, inplace=True
        )
        st.session_state.fixa = st.session_state.fixa[
            ["CONSULTOR", "STATUS", "R$ ACUMULADO", "TIPO VENDA"]
        ]

    dataframe = pd.concat([st.session_state.fixa, st.session_state.movel])
    dataframe.dropna(inplace=True)

    dataframe = dataframe[dataframe["STATUS"].isin(CONCLUIDOS_MOVEL + CONCLUIDOS_FIXA)]

    consultor = st.selectbox(
        "Selecionar Consultor", options=dataframe["CONSULTOR"].unique().tolist()
    )
    multiplicador_novos = st.number_input("Multiplicador Novos", step=0.1)
    multiplicador_portabilidade = st.number_input(
        "Multiplicador Portabilidade", step=0.1
    )
    multiplicador_ja_cliente = st.number_input("Multiplicador Já Cliente", step=0.1)
    multiplicador_migracao_pre_pos = st.number_input(
        "Multiplicador Migração Pré-Pós", step=0.1
    )
    multiplicador_fixa = st.number_input("Multiplicador Fixa", step=0.1)
    multiplicador_avancada = st.number_input("Multiplicador Avançada", step=0.1)

    df = dataframe[dataframe["CONSULTOR"] == consultor]
    faixa = df["R$ ACUMULADO"].sum()
    filtro = get_filtro(faixa)

    novos_acumulado = df[df["TIPO VENDA"].isin(NOVOS)]["R$ ACUMULADO"].sum()
    portabilidade_acumulado = df[df["TIPO VENDA"].isin(PORTABILIDADE)][
        "R$ ACUMULADO"
    ].sum()
    ja_cliente_acumulado = df[df["TIPO VENDA"].isin(JA_CLIENTE)]["R$ ACUMULADO"].sum()
    migracao_pre_pos_acumulado = df[df["TIPO VENDA"].isin(MIGRACAO_PRE_POS)][
        "R$ ACUMULADO"
    ].sum()
    avancada_acumulado = df[df["TIPO VENDA"] == "AVANÇADA"]["R$ ACUMULADO"].sum()
    fixa_acumulado = df[df["TIPO VENDA"] == "FIXA"]["R$ ACUMULADO"].sum()

    remuneracoes = [
        {
            "CONSULTOR": consultor,
            "FAIXA": faixa,
            "FILTRO": filtro,
            "*NOVOS": multiplicador_novos,
            "*PORTABILIDADE": multiplicador_portabilidade,
            "*JÁ CLIENTE": multiplicador_ja_cliente,
            "*MIGRAÇÃO PRÉ/PÓS": multiplicador_migracao_pre_pos,
            "*FIXA": multiplicador_fixa,
            "*AVANÇADA": multiplicador_avancada,
            "NOVOS": novos_acumulado,
            "PORTABILIDADE": portabilidade_acumulado,
            "JÁ CLIENTE": ja_cliente_acumulado,
            "MIGRAÇÃO PRÉ/PÓS": migracao_pre_pos_acumulado,
            "AVANÇADA": avancada_acumulado,
            "FIXA": fixa_acumulado,
            "R NOVOS": novos_acumulado * multiplicador_novos,
            "R PORTABILIDADE": portabilidade_acumulado * multiplicador_portabilidade,
            "R JÁ CLIENTE": ja_cliente_acumulado * multiplicador_ja_cliente,
            "R MIGRAÇÃO PRÉ/PÓS": migracao_pre_pos_acumulado
            * multiplicador_migracao_pre_pos,
            "R AVANÇADA": avancada_acumulado * multiplicador_avancada,
            "R FIXA": fixa_acumulado * multiplicador_fixa,
        }
    ]

    soma_r = (
        remuneracoes[0]["R NOVOS"]
        + remuneracoes[0]["R PORTABILIDADE"]
        + remuneracoes[0]["R JÁ CLIENTE"]
        + remuneracoes[0]["R MIGRAÇÃO PRÉ/PÓS"]
        + remuneracoes[0]["R AVANÇADA"]
        + remuneracoes[0]["R FIXA"]
    )

    remuneracoes[0]["R TOTAL"] = soma_r

    df_r = pd.DataFrame(remuneracoes)

    st.dataframe(df_r, hide_index=True)

