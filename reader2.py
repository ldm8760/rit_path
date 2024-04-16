import PyPDF2
import re

class reader2:
    def __init__(self) -> None:
        self.__filename: str = 'Undergrad_Course_Descriptions.pdf'
        self.page_text: str = ""
        self.matches: list[str] = []

    def inspect(self):
        with open(self.__filename, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # num_pages = reader.numPages
            # for page_num in range(num_pages):
            text = reader.pages[45].extract_text()
            # text = text.replace("\n", "\\n \n")
            self.writeToFile(text)
            print(f"Page {45 - 1}:")
            print(text)
            print("")

    def writeToFile(self, string: str) -> None:
        with open("results.txt", "w+") as f:
            f.writelines(string)


    def read(self) -> None:
        reader = PyPDF2.PdfReader(self.__filename)
        page_text = reader.pages[45].extract_text()
        # page_text = page_text.replace('\n', ' ')
        self.page_text = page_text

    def analyze(self, text: str) -> list[str]: # type: ignore
        cc = '(\w{4}-\d+)'
        description = '([\w\W\s]+?)'
        class_type = '(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)(?:\s(\d))?.{0,2}Credits (\d|\d+ - \d+)'
        seasons_parenthesis = '\((Fall|Spring|Summmer|Fall, Spring|Spring, Summer|Fall, Spring, Summer|Biannual)\)'
        full = '(\w{4}-\d+) ([\w\W\s]+?)\s+?(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)(?:\s(\d))?.{0,2}Credits (\d|\d+ - \d+) \((Fall|Spring|Summmer|Fall, Spring|Spring, Summer|Fall, Spring, Summer|Biannual)\)'
        full = '(\w{4}-\d+) ([\w\W\s\n]+?)\s+?(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)(?:\s*?(\d))?.{0,2}(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)?(?:\s*?(\d))?.{0,2}Credits (\d|\d+ - \d+) \((Fall|Spring|Summmer|Fall, Spring|Spring, Summer|Fall, Spring, Summer)\)'

        # pattern = re.compile(rf'{cc}\s+(.+?)\n([\s\S]+?)\n.*?Credits (\d+) {seasons_parenthesis}', re.MULTILINE)
        # pattern = re.compile(rf'{cc} {description}\s+?{class_type} {seasons_parenthesis}')
        full = '(\w{4}-\d+)\s(.*?)\n([\w\W\s]+?)\s+?(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)(?:\s*?(\d))?.{0,2}(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)?(?:\s*?(\d))?.{0,2}Credits (\d|\d+ - \d+) \((Fall|Spring|Summmer|Fall, Spring|Spring, Summer|Fall, Spring, Summer|Biannual)\)'
        pattern = re.compile(rf'{full}')
        matches = re.findall(pattern, text)
        self.matches = matches

def main():
    x = reader2()
    x.read()
    x.analyze(x.page_text)
    print()
    x.inspect()

    for i in x.matches:
        print(i[0:2], i[3:9])
    print(len(x.matches))




if __name__ == "__main__":
    main()