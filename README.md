PDF Blue Text Extractor

This Python script extracts blue-colored text from a PDF file, specifically after encountering a trigger phrase. The extracted text is then saved in an Excel file.

Features

Scans a PDF for text with formatting info.
Identifies and extracts blue-colored text that appears after a given trigger phrase.
Saves the extracted data into an Excel file, storing each detected segment as a new row.

Installation

Ensure you have Python installed, then install the required dependencies:
pip install pymupdf pandas openpyxl

Code Explanation
Trigger Phrase: The extraction starts after a specific phrase ("triggering_text_in_pdf" in the example). You can modify this to any other trigger phrase.
Color Filtering: The script extracts blue-colored text by checking the RGB values of the text's color. It considers text with a higher blue component than red or green as "blue."
Excel Output: All the extracted blue text is saved in an Excel file. Each line of blue text is added as a row.
Pages: The script processes each page in the PDF, collecting blue text that appears after the trigger phrase.

Usage

Modify the pdf_path and output_xls variables in the script to match your input PDF and desired Excel output filename. Example:

pdf_path = "PUT_YOUR_INPUT_PATH_HERE.pdf"
output_xls = "output.xlsx"

Dependencies

pymupdf (fitz) for handling PDFs

pandas for data manipulation

openpyxl for Excel file output

Output

The extracted data will be saved in blue_text_output_new_row_per_trigger.xlsx as a table where each row contains text extracted after the trigger phrase.
