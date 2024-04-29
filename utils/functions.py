import pandas as pd


def get_multiplier(filtro):
    multiplicadores = {
        "default": {
            "PORTABILIDADE": 0.0,
            "NOVOS": 0.0,
            "ALTAS": 0.0,
            "FIXA": 0.0,
            "AVANÇADA": 0.0
        },
        "FILTRO 1": {
            "PORTABILIDADE": 0.0,
            "NOVOS": 0.0,
            "ALTAS": 0.0,
            "FIXA": 0.6,
            "AVANÇADA": 0.7
        },
        "FILTRO 2": {
            "PORTABILIDADE": 0.5,
            "NOVOS": 0.5,
            "ALTAS": 0.3,
            "FIXA": 0.6,
            "AVANÇADA": 0.7
        },
        "FILTRO 3": {
            "PORTABILIDADE": 0.8,
            "NOVOS": 0.8,
            "ALTAS": 0.6,
            "FIXA": 0.6,
            "AVANÇADA": 0.7
        },
        "FILTRO 4": {
            "PORTABILIDADE": 1.3,
            "NOVOS": 1.0,
            "ALTAS": 0.8,
            "FIXA": 0.6,
            "AVANÇADA": 0.7
        },
        "FILTRO 5": {
            "PORTABILIDADE": 1.5,
            "NOVOS": 1.2,
            "ALTAS": 0.9,
            "FIXA": 0.6,
            "AVANÇADA": 0.7
        },
        "FILTRO 6": {
            "PORTABILIDADE": 1.7,
            "NOVOS": 1.4,
            "ALTAS": 1.0,
            "FIXA": 0.6,
            "AVANÇADA": 0.7
        }
    }

    return multiplicadores.get(filtro)


def get_filtro(faixa, tipo):
    if tipo == "Efetivo":
        if faixa <= 1000:
            return "FILTRO 1"
        elif faixa <= 1200:
            return "FILTRO 2"
        elif faixa <= 1500:
            return "FILTRO 3"
        elif faixa <= 1800:
            return "FILTRO 4"
        elif faixa <= 2100:
            return "FILTRO 5"
        else:
            return "FILTRO 6"
    elif tipo == "Estágio":
        if faixa <= 600:
            return "FILTRO 0"
        elif faixa <= 701:
            return "FILTRO 1"
        elif faixa <= 1001:
            return "FILTRO 2"
        elif faixa <= 1301:
            return "FILTRO 3"
        elif faixa <= 1601:
            return "FILTRO 4"
        elif faixa <= 1901:
            return "FILTRO 5"
        else:
            return "FILTRO 6"


def get_information_data(bonus: float, salario: float, ajuda: float, estorno: float, faixa: float):
    total = salario + ajuda + bonus
    return [
        ["TOTAL", "Ajuda de Custo", "BÔNUS", "SALÁRIO"],
        [f"R$ {faixa}", f"R$ {ajuda}", f"R$ {bonus}", f"R$ {salario}"],
        ["", "", "", ""],
        ["", "Valor a depositar", "Estorno", ""],
        ["", f"R$ {total}", f"R$ {estorno}", ""]
    ]


def get_multipliers_data(dfr: pd.DataFrame):
    return [
        ["Novos", "Multiplicador", "mult. camp", "Total"],
        [f"R$ {dfr["NOVOS"][0]:.1f}", f"{dfr["*NOVOS"][0]:.1f}", 0, f"R$ {dfr["R NOVOS"][0]:.1f}"],
        ["Portabilidade", "Multiplicador", "mult. camp", "Total"],
        [f"R$ {dfr["PORTABILIDADE"][0]:.1f}", f"{dfr["*PORTABILIDADE"][0]:.1f}", 0, f"R$ {dfr["R PORTABILIDADE"][0]:.1f}"],
        ["Já Cliente", "Multiplicador", "mult. camp", "Total"],
        [f"R$ {dfr["JÁ CLIENTE"][0]:.1f}", f"{dfr["*JÁ CLIENTE"][0]:.1f}", 0, f"R$ {dfr["R JÁ CLIENTE"][0]:.1f}"],
        ["Migração PP", "Multiplicador", "mult. camp", "Total"],
        [f"R$ {dfr["MIGRAÇÃO PRÉ/PÓS"][0]:.1f}", f"{dfr["*MIGRAÇÃO PRÉ/PÓS"][0]:.1f}", 0, f"R$ {dfr["R MIGRAÇÃO PRÉ/PÓS"][0]:.1f}"],
        ["Avançada", "Multiplicador", "mult. camp", "Total"],
        [f"R$ {dfr["AVANÇADA"][0]:.1f}", f"{dfr["*AVANÇADA"][0]:.1f}", 0, f"R$ {dfr["R AVANÇADA"][0]:.1f}"],
        ["", "", "", ""],
        ["Fixa sem deb aut", "Fator", "", "Total"],
        [f"R$ {dfr["FIXA"][0]:.1f}", f"{dfr["*FIXA"][0]:.1f}", "", f"R$ {dfr["R FIXA"][0]:.1f}"],
        ["Fixa com deb aut", "Fator", "", "Total"],
        [0, 0.9, "", 0],
        ["troca", "multiplic.", "", "total"],
        [0, 0, "", 0],
    ]
