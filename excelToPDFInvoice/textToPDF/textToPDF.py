from fpdf import FPDF
import glob
import re

filepaths = glob.glob("source/*.txt")
for file in filepaths:
    with open(file, "r") as f:
        text = f.read()
        text = re.sub(r'\[\d+]', '', text)
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_font("Helvetica", size=20)
        title = file.split("/")[-1].split(".")[0]
        pdf.cell(0, 10, txt=title.capitalize(), ln=1)
        pdf.set_font("Helvetica", size=12)
        pdf.multi_cell(0, 6, txt=text, align="L")
        pdf.output(f'dist/{title}.pdf')
