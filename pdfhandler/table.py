import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle


def create_multipliers_table(df: list) -> Table:
    # data = [df.columns.tolist()] + df.values.tolist()

    table = Table(df)
    style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
            ("BACKGROUND", (0, 2), (-1, 2), colors.lightsalmon),
            ("TEXTCOLOR", (0, 2), (-1, 2), colors.white),
            ("BACKGROUND", (0, 4), (-1, 4), "#7030A0"),
            ("TEXTCOLOR", (0, 4), (-1, 4), colors.white),
            ("BACKGROUND", (0, 6), (-1, 6), "#002060"),
            ("TEXTCOLOR", (0, 6), (-1, 6), colors.white),
            ("BACKGROUND", (0, 8), (-1, 8), "#FF6600"),
            ("TEXTCOLOR", (0, 8), (-1, 8), colors.white),
            ("BACKGROUND", (0, 11), (-1, 11), "#002060"),
            ("TEXTCOLOR", (0, 11), (-1, 11), colors.white),
            ("BACKGROUND", (0, 13), (-1, 13), "#002060"),
            ("TEXTCOLOR", (0, 13), (-1, 13), colors.white),
            ("BACKGROUND", (0, 15), (-1, 15), "#002060"),
            ("TEXTCOLOR", (0, 15), (-1, 15), colors.white),
        ]
    )

    table.setStyle(style)

    return table