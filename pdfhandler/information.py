from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle


def create_informatons_table(df: list):
    table = Table(df)
    style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), "#92D050"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
            ("BACKGROUND", (0, 3), (-1, 3), colors.grey),
        ]
    )

    table.setStyle(style)

    return table
