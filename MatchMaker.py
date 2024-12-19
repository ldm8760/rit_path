import re

class MatchMaker:
    def __init__(self) -> None:
        self.__FILENAME: str = "threadTest.txt" # 75 courses
        # self.__contents: list[str] = self.readFile()

    def readFile(self) -> list[str]:
        with open(self.__FILENAME, "r") as file:
            content = file.read()
        return self.makeMatches(content)

    def makeMatches(self, text: str) -> list[str]: 
        full = r'\s*?(\w{4}-\d+)\s(.*?)\n([\w\W\s]+?)\s+?(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)(?:\s*?(\d))?.{0,2}(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)?(?:\s*?(\d))?.{0,2}\s*?Credits\s*?(\d|\d+ - \d+)\s+?\((Fall|Spring|Summer|Fall,\s*?Spring|Spring,\s*?Summer|Fall,\s*?Spring,\s*?Summer|Biannual)\)'
        pattern = re.compile(f'{full}')
        matches = re.findall(pattern, text)
        return matches