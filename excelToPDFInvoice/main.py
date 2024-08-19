import pandas as pd
import glob
from fpdf import FPDF

filepaths = glob.glob("invoices/*.xlsx")

for file in filepaths:
    # Read data from excel
    df = pd.read_excel(file, sheet_name="Sheet 1")

    # Init pdf object
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    # Add a page and style the font
    pdf.add_page()
    pdf.set_font("Helvetica", size=16)

    # Get the invoice number from the filepath
    invoice_number = file.split('/')[-1].split('.')[:-1]
    invoice_number = '.'.join(invoice_number)

    # Write the header
    pdf.cell(w=50, h=8, txt=f'Invoice #{invoice_number.split('-')[0]}', ln=1)

    date = file.split('-')[1].split('.')[:-1]
    date = '.'.join(date)
    pdf.set_font("Helvetica", size=12)
    pdf.cell(w=50, h=8, txt=f'Date: {date}', ln=1)

    # Write to file
    pdf.output(f'PDFs/{invoice_number}.pdf')
