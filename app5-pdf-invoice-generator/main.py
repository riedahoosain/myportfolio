# A script that reads invoice records from Excel files and automatically generates PDF invoices
from fpdf import FPDF  # PDF module
import pandas as pd  # Works nicely for CSV and data files
import glob
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")
for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")
    # Creates a PDF instance
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice no. {invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")









