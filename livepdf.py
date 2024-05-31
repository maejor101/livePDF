import fitz  # PyMuPDF

def inspect_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    
    for page in doc:
        annotations = page.annots()
        for annot in annotations:
            if annot["subtype"] == "Widget":
                field_name = annot.get("TU", annot.get("T"))
                print(f"Field Name: {field_name}")
                print(f"Widget Type: {annot.get('FT')}")
                print(f"JavaScript Action: {annot.get('AA')}")  # Extract JavaScript action (if any)
    
    doc.close()

# Provide the path to your PDF file
pdf_path = r'C:\Users\DELL\Documents\ICE-DATA-CURATOR\Z95.pdf'
inspect_pdf(pdf_path)
