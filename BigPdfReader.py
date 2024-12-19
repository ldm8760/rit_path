import PyPDF2

class BigPdfReader:
    def __init__(self, pageNumber: int = 45) -> None:
        self.__INPUT_FILENAME: str = 'Undergrad_Course_Descriptions.pdf'
        self.__OUTPUT_FILENAME: str = 'threadTest.txt'
        self.__pageNumber: int = pageNumber

    def getOutputFilename(self) -> str:
        return self.__OUTPUT_FILENAME

    def readPdf(self) -> None:
        with open(self.__INPUT_FILENAME, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            page_text = reader.pages[self.__pageNumber + 1].extract_text()
            self.writeTextFile(page_text)

    def writeTextFile(self, string: str) -> None:
        with open(self.__OUTPUT_FILENAME, "a") as f:
            f.writelines(string)

def main():
    with open(BigPdfReader().getOutputFilename(), 'w') as f: 
        pass

    for i in range(40, 47, 1):
        t = BigPdfReader(i)
        t.readPdf()

    print("Complete!")

if __name__ == "__main__":
    main()