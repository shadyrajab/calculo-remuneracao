from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph


def create_statement_paragraph() -> Paragraph:
    style = getSampleStyleSheet()["Normal"]
    style.alignment = 1
    statement = Paragraph(
        """
            Por ser verdade, firmo o presente documento. Dando plena quitação de débitos.<br/>
            <br/>
            Data: ____/____/____
        """,
        style,
    )

    return statement
