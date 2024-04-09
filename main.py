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
    MOVEL = pd.read_excel(planilha, index_col=[0], sheet_name="MOVEL")
    FIXA = pd.read_excel(planilha, index_col=[0], sheet_name="FIXA_E_AVANÇADA")

    MOVEL = MOVEL[MOVEL["STATUS"].isin(CONCLUIDOS_MOVEL)]
    FIXA = FIXA[FIXA["STATUS"].isin(CONCLUIDOS_FIXA)]

    FIXA["R$ ACUMULADO"] = FIXA["QUANTIDADE"] * FIXA["VALOR DO PLANO"]
    FIXA.rename(columns={"TIPO DE VENDA": "TIPO VENDA"}, inplace=True)

    MOVEL = MOVEL[["CONSULTOR", "STATUS", "R$ ACUMULADO", "TIPO VENDA"]]
    FIXA = FIXA[["CONSULTOR", "STATUS", "R$ ACUMULADO", "TIPO VENDA"]]

    dataframe = pd.concat([FIXA, MOVEL])
    dataframe.dropna(inplace=True)

    faixas = []

    for consultor in dataframe["CONSULTOR"].unique().tolist():
        df = dataframe[dataframe["CONSULTOR"] == consultor]
        faixa = df["R$ ACUMULADO"].sum()
        filtro = get_filtro(faixa)

        novos_acumulado = df[df["TIPO VENDA"].isin(NOVOS)]["R$ ACUMULADO"].sum()
        portabilidade_acumulado = df[df["TIPO VENDA"].isin(PORTABILIDADE)][
            "R$ ACUMULADO"
        ].sum()
        ja_cliente_acumulado = df[df["TIPO VENDA"].isin(JA_CLIENTE)][
            "R$ ACUMULADO"
        ].sum()
        migracao_pre_pos_acumulado = df[df["TIPO VENDA"].isin(MIGRACAO_PRE_POS)][
            "R$ ACUMULADO"
        ].sum()
        avancada_acumulado = df[df["TIPO VENDA"] == "AVANÇADA"]["R$ ACUMULADO"].sum()
        fixa_acumulado = df[df["TIPO VENDA"] == "FIXA"]["R$ ACUMULADO"].sum()

        novos_multiplicador = MULTIPLICADORES.get(filtro)["NOVOS"]
        portabilidade_multiplicador = MULTIPLICADORES.get(filtro)["PORTABILIDADE"]
        ja_cliente_multiplicador = MULTIPLICADORES.get(filtro)["JÁ CLIENTE"]
        migracao_pre_pos_multiplicador = MULTIPLICADORES.get(filtro)["MIGRAÇÃO PRÉ/PÓS"]
        avancada_multiplicador = MULTIPLICADORES.get(filtro)["AVANÇADA"]
        fixa_multiplicador = MULTIPLICADORES.get(filtro)["FIXA"]

        faixas.append(
            {
                "CONSULTOR": consultor,
                "FAIXA": faixa,
                "FILTRO": filtro,
                "*NOVOS": novos_multiplicador,
                "*PORTABILIDADE": portabilidade_multiplicador,
                "*JÁ CLIENTE": ja_cliente_multiplicador,
                "*MIGRAÇÃO PRÉ/PÓS": migracao_pre_pos_multiplicador,
                "*FIXA": fixa_multiplicador,
                "*AVANÇADA": avancada_multiplicador,
                "NOVOS": novos_acumulado,
                "PORTABILIDADE": portabilidade_acumulado,
                "JÁ CLIENTE": ja_cliente_acumulado,
                "MIGRAÇÃO PRÉ/PÓS": migracao_pre_pos_acumulado,
                "AVANÇADA": avancada_acumulado,
                "FIXA": fixa_acumulado,
                "R NOVOS": novos_acumulado * novos_multiplicador,
                "R PORTABILIDADE": portabilidade_acumulado
                * portabilidade_multiplicador,
                "R JÁ CLIENTE": ja_cliente_acumulado * ja_cliente_multiplicador,
                "R MIGRAÇÃO PRÉ/PÓS": migracao_pre_pos_acumulado
                * migracao_pre_pos_multiplicador,
                "R AVANÇADA": avancada_acumulado * avancada_multiplicador,
                "R FIXA": fixa_acumulado * fixa_multiplicador,
            }
        )

        soma_r = (
            faixas[-1]["R NOVOS"]
            + faixas[-1]["R PORTABILIDADE"]
            + faixas[-1]["R JÁ CLIENTE"]
            + faixas[-1]["R MIGRAÇÃO PRÉ/PÓS"]
            + faixas[-1]["R AVANÇADA"]
            + faixas[-1]["R FIXA"]
        )

        faixas[-1]["SOMA R"] = soma_r

    if len(faixas) >= 1:
        df_faixas = pd.DataFrame(faixas)

    st.dataframe(df_faixas)
