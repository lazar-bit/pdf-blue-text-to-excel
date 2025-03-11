PDF Blue Text Extractor

This Python script extracts blue-colored text from a PDF file, specifically after encountering a trigger phrase. The extracted text is then saved in an Excel file.

Features

Scans a PDF for text with formatting info.

Identifies and extracts blue-colored text that appears after a given trigger phrase.

Saves the extracted data into an Excel file, storing each detected segment as a new row.

Installation

Ensure you have Python installed, then install the required dependencies:

pip install pymupdf pandas openpyxl

Usage

Modify the pdf_path and output_xls variables in the script to match your input PDF and desired Excel output filename. Example:

pdf_path = "PUT_YOUR_INPUT_PATH_HERE.pdf"
output_xls = "output.xlsx"

Then run:

python script.py

Dependencies

pymupdf (fitz) for handling PDFs

pandas for data manipulation

openpyxl for Excel file output

Output

The extracted data will be saved in blue_text_output_new_row_per_trigger.xlsx as a table where each row contains text extracted after the trigger phrase.
