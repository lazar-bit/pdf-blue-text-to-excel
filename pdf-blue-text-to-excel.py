import fitz  # PyMuPDF
import pandas as pd

def extract_blue_after_trigger(pdf_path, output_xls):
    doc = fitz.open(pdf_path)
    data = []  # To store rows of blue text after each trigger
    new_entry_trigger = "triggering_text_in_pdf"  # Trigger phrase
    collecting = False  # Flag to start collecting after the trigger
    current_row = []  # Temporary list to store the current row of blue text

    for page_num, page in enumerate(doc):
        print(f"--- Processing Page {page_num + 1} ---")
        text_instances = page.get_text("dict")  # Extract text with formatting info
        
        for block in text_instances["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    color = span["color"]  # Extract color info
                    
                    # Debugging: Print text and color
                    print(f"Text: {text}, Color: {color}")

                    # Start collecting after the trigger phrase
                    if new_entry_trigger in text:
                        if current_row:  # If there is any blue text, save it to data before starting a new row
                            data.append(current_row)
                        current_row = []  # Start a new row
                        collecting = True  # Start collecting after the trigger phrase
                        continue  # Skip the trigger line
                    
                    # Extract RGB components from the color value
                    red = (color >> 16) & 0xFF  # Extract red component
                    green = (color >> 8) & 0xFF  # Extract green component
                    blue = color & 0xFF  # Extract blue component

                    # If collecting, capture non-black (blue) text
                    if collecting and blue > red and blue > green:  # Blue text (not black)
                        print(f"Captured Blue Text: {text}")
                        current_row.append(text)  # Add blue text to the current row

    # After the last page, append the last row if it exists
    if current_row:
        data.append(current_row)

    # Save the captured blue text as rows in the Excel file
    df = pd.DataFrame(data)  # Store all rows of blue text
    df.to_excel(output_xls, index=False, header=False)  # No headers, just data in rows
    print(f"Extraction complete! Data saved to {output_xls}")

# Usage
pdf_path = "your_file.pdf"  # Your file path
output_xls = "blue_text_output_new_row_per_trigger.xlsx"
extract_blue_after_trigger(pdf_path, output_xls)
