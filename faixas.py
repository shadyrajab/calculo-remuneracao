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


MULTIPLICADORES = {
    "FILTRO 1": {
        "NOVOS": 0,
        "PORTABILIDADE": 0,
        "JÁ CLIENTE": 0,
        "MIGRAÇÃO PRÉ/PÓS": 0.4,
        "FIXA": 0.6,
        "AVANÇADA": 0.7,
    },
    "FILTRO 2": {
        "NOVOS": 0.5,
        "PORTABILIDADE": 0.5,
        "JÁ CLIENTE": 0.3,
        "MIGRAÇÃO PRÉ/PÓS": 0.4,
        "FIXA": 0.6,
        "AVANÇADA": 0.7,
    },
    "FILTRO 3": {
        "NOVOS": 0.8,
        "PORTABILIDADE": 0.8,
        "JÁ CLIENTE": 0.6,
        "MIGRAÇÃO PRÉ/PÓS": 0.4,
        "FIXA": 0.6,
        "AVANÇADA": 0.7,
    },
    "FILTRO 4": {
        "NOVOS": 1.3,
        "PORTABILIDADE": 1.0,
        "JÁ CLIENTE": 0.8,
        "MIGRAÇÃO PRÉ/PÓS": 0.4,
        "FIXA": 0.6,
        "AVANÇADA": 0.7,
    },
    "FILTRO 5": {
        "NOVOS": 1.5,
        "PORTABILIDADE": 1.2,
        "JÁ CLIENTE": 0.9,
        "MIGRAÇÃO PRÉ/PÓS": 0.4,
        "FIXA": 0.6,
        "AVANÇADA": 0.7,
    },
    "FILTRO 6": {
        "NOVOS": 1.7,
        "PORTABILIDADE": 1.4,
        "JÁ CLIENTE": 1.0,
        "MIGRAÇÃO PRÉ/PÓS": 0.4,
        "FIXA": 0.6,
        "AVANÇADA": 0.7,
    },
}
