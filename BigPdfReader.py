import PyPDF2

INPUT_FILENAME: str = 'data/Undergrad_Course_Descriptions.pdf'
OUTPUT_FILENAME: str = 'data/textdump.txt'


def extract_info():
    with open(INPUT_FILENAME, 'rb') as input:
        reader = PyPDF2.PdfReader(input)
        total = len(reader.pages)

        pageNumber = 0
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output:
            while pageNumber < total:
                page_text = reader.pages[pageNumber].extract_text()
                output.writelines(page_text)
                pageNumber += 1

if __name__ == "__main__":
    extract_info()
    print("Complete!")