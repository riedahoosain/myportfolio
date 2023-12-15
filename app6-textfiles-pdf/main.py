# Reads text files in files/ and then extracts data to multipage PDF file

from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("files/*.txt")

# Creates PDF instance
pdf = FPDF(orientation="P", unit="mm", format="A4")


for filepath in filepaths:
    # Adds a new page for each filename
    pdf.add_page()

    # extracts file name minus extenstions
    filenames = Path(filepath).stem

    with open(filepath, 'r') as file:
        data = file.read()

    # Writes the the first filename to the instance
    # Converts to title case eg Cats instead of cats
    pdf.set_font(family="Times", style="B", size=20)
    pdf.cell(w=50, h=8, txt=filenames.title(), ln=1)
    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=10, txt=data)

# Saves instance with all data to one PDF file
# Saves to the same folder where main file is
try:
    pdf.output("output.pdf")
    print("""
    ###############################
    PDF file output.pdf was created.
    ###############################
    """)
except PermissionError:
    print("""
    ####################
    File was not created.
    Please make sure that output.pdf is not open at the moment.
    ####################
          """)
