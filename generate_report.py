import pandas as pd
from fpdf import FPDF

# Read data
data = pd.read_csv('data.csv')

# Analyze data
total_sales = data['Sales'].sum()
average_sales = data['Sales'].mean()

# Create PDF
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Sales Report', ln=True, align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

pdf = PDFReport()
pdf.add_page()

pdf.set_font("Arial", size=12)

# Add summary
pdf.cell(0, 10, f'Total Sales: ${total_sales}', ln=True)
pdf.cell(0, 10, f'Average Sales: ${average_sales:.2f}', ln=True)
pdf.ln(10)

# Add table header
pdf.set_font('Arial', 'B', 12)
pdf.cell(40, 10, 'Name', 1)
pdf.cell(40, 10, 'Sales', 1)
pdf.cell(40, 10, 'Region', 1)
pdf.ln()

# Add table rows
pdf.set_font('Arial', '', 12)
for idx, row in data.iterrows():
    pdf.cell(40, 10, str(row['Name']), 1)
    pdf.cell(40, 10, str(row['Sales']), 1)
    pdf.cell(40, 10, str(row['Region']), 1)
    pdf.ln()

# Save PDF
pdf.output('sales_report.pdf')

print("Report generated: sales_report.pdf")
