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
            ("BACKGROUND", (0, 5), (-1, 5), colors.grey),
            ("BACKGROUND", (0, 8), (-1, 8), colors.grey),
            ("BACKGROUND", (0, 10), (-1, 10), "#00B0F0"),
        ]
    )

    table.setStyle(style)

    return table
