from reportlab.platypus import Table, TableStyle


def create_account_table(ag: str, conta: str, tipo: str):
    data = [["Agência", "Conta", "Tipo"], [ag, conta, tipo]]

    table = Table(data)
    style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), "#00FF00"),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ]
    )

    table.setStyle(style)

    return table
