# Automated-Report-Generation

**Company** - CODETECH IT SOLUTIONS

**Name** - Tanmoy Das

**Intern ID** - CT06DR1738

**Domain** - Python Programming

**Duration** - 6 weeks

**Mentor** - Neela Santosh

This Python script is designed to read a table from a text file and generate a PDF report containing that table. It is a practical tool for converting plain text data into a professional-looking, portable document format that can be shared or archived. The script is structured into two main parts: parsing the table from the text file and generating a PDF from the parsed data.

**Tools and Libraries Used**

* **FPDF** - The main library used in this script is FPDF, which is a Python library for creating PDF documents. FPDF allows you to create pages, set fonts, insert text, and add tables in a flexible manner. It is lightweight and easy to use for simple PDF generation tasks, making it ideal for turning text or data into formatted reports.

* **Python Built-in Functions** - The script also uses Python’s built-in functions for file handling, string manipulation, and list processing. Functions like open(), readlines(), and strip() are used to read the input text file and clean the data. These functions are essential for parsing and preparing the table for PDF output.

**How the Script Works**
* **Parsing the Table from the Text File**

The first part of the script is the function parse_table_from_txt(file_path). This function reads the contents of a text file, processes each line, and returns a structured table in the form of a list of lists.

The script opens the text file in read mode with UTF-8 encoding, ensuring that any special characters are handled correctly.

It reads all lines into memory and iterates over them. Each line is stripped of leading and trailing whitespace to ensure that empty spaces don’t interfere with the table formatting.

Empty lines are ignored, which allows the script to handle text files with inconsistent spacing or blank lines.

Each line is then split into individual cells. If the line contains commas, the function uses them as separators (common in CSV-like files). Otherwise, it splits the line using whitespace, which is useful for plain text tables that use spaces or tabs.

Finally, each row is appended to a list, creating a complete table that the script can later use for PDF generation.

* **Generating the PDF**

The second part of the script is the function table_to_pdf(table, output_pdf). This function takes the parsed table and creates a PDF file that visually represents the data in a clean tabular format.

The function starts by creating an FPDF object and adding a new page. It also sets automatic page breaks to ensure that the table does not overflow the page.

The title of the PDF, "Table Report from TXT File," is added at the top of the page in bold and centered. This provides a clear header for the document.

The script sets the font for the table content and calculates the width of each column dynamically based on the number of columns in the table. This ensures that the table fits neatly on the page regardless of how many columns there are.

It iterates through each row of the table and adds each cell as a table cell in the PDF, drawing borders around them for clarity. After writing all columns of a row, it moves to the next line.

Finally, the PDF is saved with the specified output filename, and the script prints a success message confirming the PDF has been created.

**Real-Life Applications**

This script can be extremely useful in real-life scenarios where data needs to be shared or archived in a readable format. Some examples include -

* **Business Reports** - Companies often store data in text files or CSVs. This script can convert such files into professional PDFs for meetings or reporting.

* **Academic Work** - Students or researchers can turn lab results, experimental data, or tabulated notes into clean PDFs for submission or presentation.

* **Inventory Management** - Small businesses can maintain stock lists or order logs in text files and generate quick PDF reports for record-keeping.

* **Automation** - This script can be part of an automated workflow where daily or weekly data is converted into reports without manual intervention.

**Conclusion**

Overall, this script demonstrates a practical workflow for converting raw text data into a professional PDF report. By combining Python’s file handling capabilities with the FPDF library, it provides a flexible and reliable way to generate readable, shareable documents from plain text. With minor modifications, it could handle more complex tables, include styling, add multiple pages, or even integrate charts, making it a powerful tool for data presentation in real life.

