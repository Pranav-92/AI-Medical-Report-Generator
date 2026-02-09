import pdfplumber

def extract_pdf_lines(pdf_file):
    extracted = []

    with pdfplumber.open(pdf_file) as pdf:
        for page_no, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if not text:
                continue
            for line in text.split("\n"):
                extracted.append({
                    "text": line.strip(),
                    "page_no": page_no
                })

    return extracted
