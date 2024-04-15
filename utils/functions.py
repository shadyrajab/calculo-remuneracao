import pandas as pd


def get_filtro(faixa):
    if faixa <= 1000:
        filtro = "FILTRO 1"

    if faixa >= 1001 and faixa <= 1200:
        filtro = "FILTRO 2"

    if faixa >= 1201 and faixa <= 1500:
        filtro = "FILTRO 3"

    if faixa >= 1501 and faixa <= 1800:
        filtro = "FILTRO 4"

    if faixa >= 1801 and faixa <= 2100:
        filtro = "FILTRO 5"

    if faixa >= 2100:
        filtro = "FILTRO 6"

    return filtro


def get_information_data(bonus: float, salario: float, ajuda: float, estorno: float):
    total = salario + ajuda + bonus
    return [
        ["", "", "BÔNUS", "", ""],
        ["", "", f"R$ {bonus}", "", ""],
        ["", "", "", "", ""],
        ["", "", "SALÁRIO", "", ""],
        ["", "", f"R$ {salario}", "", ""],
        ["", "", "Ajuda de Custo", "", ""],
        ["", "", f"R$ {ajuda}", "", ""],
        ["", "", "", "", ""],
        ["", "", "Estorno", "", ""],
        ["", "", f"R$ {estorno}", "", ""],
        ["", "", "Valor a depositar", "", ""],
        ["", "", f"R$ {total}", "", ""],
    ]


def get_multipliers_data(dfr: pd.DataFrame):
    return [
        ["Novos", "Multiplicador", "mult. camp", "Total"],
        [f"R$ {dfr["NOVOS"][0]:.1f}", f"R$ {dfr["*NOVOS"][0]:.1f}", 0, f"R$ {dfr["R NOVOS"][0]:.1f}"],
        ["Portabilidade", "Multiplicador", "mult. camp", "Total"],
        [f"R$ {dfr["PORTABILIDADE"][0]:.1f}", f"R$ {dfr["*PORTABILIDADE"][0]:.1f}", 0, f"R$ {dfr["R PORTABILIDADE"][0]:.1f}"],
        ["Já Cliente", "Multiplicador", "mult. camp", "Total"],
        [f"R$ {dfr["JÁ CLIENTE"][0]:.1f}", f"R$ {dfr["*JÁ CLIENTE"][0]:.1f}", 0, f"R$ {dfr["R JÁ CLIENTE"][0]:.1f}"],
        ["Migração PP", "Multiplicador", "mult. camp", "Total"],
        [f"R$ {dfr["MIGRAÇÃO PRÉ/PÓS"][0]:.1f}", f"R$ {dfr["*MIGRAÇÃO PRÉ/PÓS"][0]:.1f}", 0, f"R$ {dfr["R MIGRAÇÃO PRÉ/PÓS"][0]:.1f}"],
        ["Avançada", "Multiplicador", "mult. camp", "Total"],
        [f"R$ {dfr["AVANÇADA"][0]:.1f}", f"R$ {dfr["*AVANÇADA"][0]:.1f}", 0, f"R$ {dfr["R AVANÇADA"][0]:.1f}"],
        ["", "", "", ""],
        ["Fixa sem deb aut", "Fator", "", "Total"],
        [f"R$ {dfr["FIXA"][0]:.1f}", f"R$ {dfr["*FIXA"][0]:.1f}", "", f"R$ {dfr["R FIXA"][0]:.1f}"],
        ["Fixa com deb aut", "Fator", "", "Total"],
        [0, 0.9, "", 0],
        ["troca", "multiplic.", "", "total"],
        [0, 0, "", 0],
    ]
