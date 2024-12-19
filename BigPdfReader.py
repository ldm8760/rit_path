import PyPDF2

class BigPdfReader:
    def __init__(self, pageNumber: int = 45) -> None:
        self.__INPUT_FILENAME: str = 'Undergrad_Course_Descriptions.pdf'
        self.__OUTPUT_FILENAME: str = 'threadTest.txt'
        self.__pageNumber: int = pageNumber

    def extract_page(self) -> None:
        with open(self.__INPUT_FILENAME, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            page_text = reader.pages[self.__pageNumber + 1].extract_text()
            with open(self.__OUTPUT_FILENAME, "a") as file2:
                file2.writelines(page_text)

def main():
    for i in range(40, 47, 1):
        t = BigPdfReader(i)
        t.extract_page()

    print("Complete!")

if __name__ == "__main__":
    main()