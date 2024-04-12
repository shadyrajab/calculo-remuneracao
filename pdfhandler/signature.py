from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph


def create_signature_paragraph(consultor: str) -> Paragraph:
    style = getSampleStyleSheet()["Normal"]
    style.alignment = 1
    signature = Paragraph(
        f"""
            ___________________________________________________________________ <br/>
            <center>{consultor.title()}</center>
        """,
        style,
    )

    return signature
