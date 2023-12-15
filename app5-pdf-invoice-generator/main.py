# A script that reads invoice records from Excel files and automatically generates PDF invoices
from fpdf import FPDF  # PDF module
import pandas as pd  # Works nicely for CSV and data files
import glob
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")
for filepath in filepaths:    
    # Creates a PDF instance
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")
    
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice no. {invoice_nr}",ln=1)

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Add a header
    columns = df.columns

    #Change _ to spaces and Capitalize
    columns = [item.replace("_", " ").title() for item in columns]
    
    pdf.set_font(family="Times", size=10, style="BU")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2],border=1)
    pdf.cell(w=30, h=8, txt=columns[3],border=1)
    pdf.cell(w=30, h=8, txt=columns[4],border=1, ln=1)

    # Add rows
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]),border=1, ln=1)


    pdf.output(f"PDFs/{filename}.pdf")









