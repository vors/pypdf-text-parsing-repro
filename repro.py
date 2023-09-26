from pypdf import PdfReader

reader = PdfReader("input.pdf")
page = reader.pages[0]
page.extract_text()
