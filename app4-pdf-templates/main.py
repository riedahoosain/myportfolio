# A script that generates PDF templates of multiple pages given some predefined guidelines
# Generates pages with lines and data
from fpdf import FPDF  # PDF module
import pandas as pd  # Works nicely for CSV and data files

# Creates a PDF instance
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Loads CSV File
df = pd.read_csv("topics.csv")
# Loops thorough the data creating pages for each info based on number pages needed
# The data contains the amount pages needed

for index, row in df.iterrows():

    # Set the Header
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 100, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    #pdf.line(10, 21, 200, 21)
    for y in range(20,300,10):
       
        pdf.line(10, y, 200, y)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(0, 100, 0)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(0, 100, 0)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for y in range(20,300,10):
       
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
print("File was created")
