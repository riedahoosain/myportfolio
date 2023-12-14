# A script that reads invoice records from Excel files and automatically generates PDF invoices
from fpdf import FPDF  # PDF module
import pandas as pd  # Works nicely for CSV and data files
import glob

filepaths = glob.glob("invoices/*.xlsx")
for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")
    




