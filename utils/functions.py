import pandas as pd


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
        else:
            return "FILTRO 5"
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

    
    if tipo == "Estágio":
        if faixa <= 600:
            filtro = "FILTRO 0"
        
        if faixa >= 601 and faixa <= 701:
            filtro = "FILTRO 1"

        if faixa >= 702 and faixa <= 1001:
            filtro = "FILTRO 2"

        if faixa >= 1002 and faixa <= 1301:
            filtro = "FILTRO 3"

        if faixa >= 1302 and faixa <= 1601:
            filtro = "FILTRO 3"

        if faixa >= 1602 and faixa <= 1901:
            filtro = "FILTRO 5"

        if faixa >= 1902:
            filtro = "FILTRO 6" 

        return filtro


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
