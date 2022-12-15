import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .consts import CARDS_PDF_FILE_NAME


def print_pdf_grid(ready_to_print_table):
    pdfmetrics.registerFont(TTFont('FreeSans', '../fonts/FreeSans.ttf'))
    doc = SimpleDocTemplate(
        f"{CARDS_PDF_FILE_NAME}",
        pagesize=A4,
        leftMargin=0,
        rightMargin=0,
        topMargin=-3,
        bottomMargin=0
    )
    items = []
    table = Table(
        ready_to_print_table,
        colWidths=200,
        rowHeights=104
    )
    set_table_styles(table)
    items.append(table)
    doc.build([table])

def set_table_styles(table):
    table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'FreeSans'),
            ('FONT', (0, 0), (-1, 0), 'FreeSans'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('INNERGRID', (0, 0), (-1, -1), 2, colors.black),
            ('BOX', (0, 0), (-1, -1), 2, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))

