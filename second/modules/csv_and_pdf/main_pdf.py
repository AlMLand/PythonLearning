import PyPDF2


def find_pages_by(query: str):
    with open('Working_Business_Proposal.pdf', mode='rb') as pdf_to_read:
        reader = PyPDF2.PdfReader(pdf_to_read)
        print(f"Number of read pages: {len(reader.pages)}")

        with open("searched_pages.pdf", mode='wb') as pdf_to_write:
            writer = PyPDF2.PdfWriter()

            for page in reader.pages:
                if query in page.extract_text():
                    writer.add_page(page)
            writer.write(pdf_to_write)

        print("Done!")


find_pages_by('worldwide')
