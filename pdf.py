from fpdf import FPDF

def parse_table_from_txt(file_path):
    """Reads a table from a txt file and returns a list of rows."""
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    table = []
    for line in lines:
        clean = line.strip()

        if clean == "":
            continue

        if "," in clean:
            row = clean.split(",")
        else:
            row = clean.split()

        table.append(row)
    return table


def table_to_pdf(table, output_pdf):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Table Report from TXT File", ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Arial", size=12)


    col_width = pdf.w / (len(table[0]) + 1)

    for i, row in enumerate(table):
        for col in row:
            pdf.cell(col_width, 10, col, border=1)
        pdf.ln()

    pdf.output(output_pdf)
    print(f"PDF successfully created: {output_pdf}")


input_file = "input.txt"
output_file = "input_report.pdf"

table_data = parse_table_from_txt(input_file)
table_to_pdf(table_data, output_file)
