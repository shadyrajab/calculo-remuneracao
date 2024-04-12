from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate 


def build_pdf_file(elements: list):
    pdf = SimpleDocTemplate("remunerações.pdf", pagesize=letter)
    pdf.build(elements)
