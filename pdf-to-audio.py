import sys
from PyPDF2 import PdfReader, PdfWriter
# print(sys.argv)
INPUT_PDF_NAME = '2023_TaxReturn.pdf'
page_num = int(sys.argv[1])

with open(INPUT_PDF_NAME, "rb") as infile:
    reader = PdfReader(infile)
    writer = PdfWriter()
    page_to_extract = reader.pages[page_num]
    writer.add_page(page_to_extract)
    output_file_name = INPUT_PDF_NAME.replace(".pdf", f"_pg_{page_num}.pdf")
    with open(output_file_name, "wb") as outfile:
        writer.write(outfile)
