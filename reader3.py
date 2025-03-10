import re
import csv

INPUT_FILE = "textdump.txt"

def makeMatches(text: str) -> None: 
    full = r'\s*?(\w{4}-\d{3}[AHRB]?)\s(.*?)\n([\w\W\s]+?)\s+?(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP|Studio|Activity)(?:\s*?(\d))?.{0,2}(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)?(?:\s*?(\d))?.{0,2}\s*?Credits\s*?(\d|\d+ - \d+)\s+?\((Fall|Spring|Summer|Fall,\s*?Spring|Spring,\s*?Summer|Fall,\s*?Spring,\s*?Summer|Fall\s*?or\s*?Spring|Biannual)\)'
    pattern = re.compile(f'{full}')
    matches = re.findall(pattern, text)
    with open("data.csv", "w", encoding="utf-8") as f:
        csvwrtiter = csv.writer(f)
        csvwrtiter.writerow(["Code", "Title", "Description", "Class1Type", "Class1TypeHours", "Class2Type", "Class2TypeHours", "Credits", "Season"])
        csvwrtiter.writerows(matches)

if __name__ == "__main__":
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        content = file.read()
    makeMatches(content)