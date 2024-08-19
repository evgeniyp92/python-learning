import pandas as pd
import glob
from fpdf import FPDF

filepaths = glob.glob("invoices/*.xlsx")

for file in filepaths:
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

    # Read data from excel
    df = pd.read_excel(file, sheet_name="Sheet 1")

    headers = df.columns.tolist()

    headers = [item.replace('_', ' ').title() for item in headers]

    pdf.set_font('Helvetica', size=10, style='B')
    pdf.cell(w=30, h=8, txt=f'{headers[0]}', border=1)
    pdf.cell(w=70, h=8, txt=f'{headers[1]}', border=1)
    pdf.cell(w=30, h=8, txt=f'{headers[2]}', border=1)
    pdf.cell(w=30, h=8, txt=f'{headers[3]}', border=1)
    pdf.cell(w=30, h=8, txt=f'{headers[4]}', border=1, ln=1)
    pdf.set_font(family='Helvetica', size=12, style='')

    # pdf.set_font('Helvetica', size=12, style='B')
    # pdf.cell(w=30, h=8, txt=f'Product ID', border=1)
    # pdf.cell(w=70, h=8, txt=f'Product Name', border=1)
    # pdf.cell(w=30, h=8, txt=f'Amount', border=1)
    # pdf.cell(w=30, h=8, txt=f'Price/Unit', border=1)
    # pdf.cell(w=30, h=8, txt=f'Total', border=1, ln=1)
    # pdf.set_font(family='Helvetica', size=12, style='')

    for index, row in df.iterrows():
        pdf.cell(w=30, h=8, txt=f'{row["product_id"]}', border=1)
        pdf.cell(w=70, h=8, txt=f'{row["product_name"]}', border=1)
        pdf.cell(w=30, h=8, txt=f'{row["amount_purchased"]}', border=1)
        pdf.cell(w=30, h=8, txt=f'{row["price_per_unit"]}', border=1)
        pdf.cell(w=30, h=8, txt=f'{row["total_price"]}', border=1, ln=1)

    pdf.set_font(family='Helvetica', style='B')
    pdf.cell(w=0, h=8, txt="Prolaps Motorsports", ln=1)

    # Write to file
    pdf.output(f'PDFs/{invoice_number}.pdf')
