import re

class reader3:
    def __init__(self) -> None:
        self.filename: str = "results.txt"
        self.__contents: str = ""

    def read(self) -> None:
        with open(self.filename, "r") as f:
            self.__contents = f.read()

    def getContents(self) -> str:
        return self.__contents

    def analyze(self, text: str) -> list[str]: 
        cc = '(\w{4}-\d+)'
        title = '\s(.*?)\n'
        description = '([\w\W\s]+?)'
        class_type = '(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)(?:\s(\d))?.{0,2}Credits (\d|\d+ - \d+)'
        seasons_parenthesis = '\((Fall|Spring|Summer|Fall, Spring|Spring, Summer|Fall, Spring, Summer|Biannual)\)'
        full = '(\w{4}-\d+) ([\w\W\s]+?)\s+?(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)(?:\s(\d))?.{0,2}Credits (\d|\d+ - \d+) \((Fall|Spring|Summer|Fall, Spring|Spring, Summer|Fall, Spring, Summer|Biannual)\)'
        full = '(\w{4}-\d+) ([\w\W\s]+?)\s+?(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)(?:\s*?(\d))?.{0,2}(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)?(?:\s*?(\d))?.{0,2}Credits (\d|\d+ - \d+) \((Fall|Spring|Summer|Fall, Spring|Spring, Summer|Fall, Spring, Summer)\)'

        # pattern = re.compile(rf'{cc}\s+(.+?)\n([\s\S]+?)\n.*?Credits (\d+) {seasons_parenthesis}', re.MULTILINE)
        # pattern = re.compile(rf'{cc} {description}\s+?{class_type} {seasons_parenthesis}')
        # adjust this later if needed
        full = '\s*?(\w{4}-\d+)\s(.*?)\n([\w\W\s]+?)\s+?(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)(?:\s*?(\d))?.{0,2}(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)?(?:\s*?(\d))?.{0,2}\s*?Credits\s*?(\d|\d+ - \d+)\s+?\((Fall|Spring|Summer|Fall,\s*?Spring|Spring,\s*?Summer|Fall,\s*?Spring,\s*?Summer|Biannual)\)'
        pattern = re.compile(rf'{full}')
        matches = re.findall(pattern, text)
        # print(len(matches))
        return matches
            
def main():
    r = reader3()
    r.read()
    tl = r.analyze(r.getContents())
    for course in tl:
        print(course[0:2], course[3:9])

if __name__ == "__main__":
    main()