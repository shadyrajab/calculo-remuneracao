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
