from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table


def build_pdf_file(multipliers: Table, statement: Paragraph, signature: Paragraph):
    pdf = SimpleDocTemplate("remunerações.pdf", pagesize=letter)
    pdf.build([multipliers, statement, signature])
