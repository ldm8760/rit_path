import PyPDF2

INPUT_FILENAME: str = 'Undergrad_Course_Descriptions.pdf'
OUTPUT_FILENAME: str = 'textdump.txt'


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

def main():
    extract_info()
    print("Complete!")

if __name__ == "__main__":
    main()