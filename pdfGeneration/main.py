import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

def draw_lines(num_steps):
    for i in range(num_steps):
        pdf.line(10, 21 + (i * 10), 200, 21 + (i * 10))

df = pd.read_csv('topics.csv')
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Helvetica", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # pdf.line(10, 21, 200, 21)
    draw_lines(27)
    pdf.ln(260)
    pdf.set_font(family="Helvetica", size=8, style="I")
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        draw_lines(27)
        pdf.ln(272)
        pdf.set_font(family="Helvetica", size=8, style="I")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

pdf.output("output.pdf")
