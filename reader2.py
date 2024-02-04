import PyPDF2
import re

def read():
    reader = PyPDF2.PdfReader('rit_path/Undergrad_Course_Descriptions.pdf')
    page_text = reader.pages[112].extract_text()
    modified_string = page_text.replace('\n', ' ')
    return modified_string

def analyze(text: str) -> list[any]:
    cc = '(\w{4}-\d+)'
    description = '([\w\W\s]+?)'
    class_type = '(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)(?:\s(\d))?.{0,2}Credits (\d|\d+ - \d+)'
    seasons_parenthesis = '\((Fall|Spring|Summmer|Fall, Spring|Spring, Summer|Fall, Spring, Summer|Biannual)\)'
    full = '(\w{4}-\d+) ([\w\W\s]+?)\s+?(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)(?:\s(\d))?.{0,2}Credits (\d|\d+ - \d+) \((Fall|Spring|Summmer|Fall, Spring|Spring, Summer|Fall, Spring, Summer|Biannual)\)'
    full = '(\w{4}-\d+) ([\w\W\s]+?)\s+?(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)(?:\s*?(\d))?.{0,2}(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind\s*?Study|CO OP)?(?:\s*?(\d))?.{0,2}Credits (\d|\d+ - \d+) \((Fall|Spring|Summmer|Fall, Spring|Spring, Summer|Fall, Spring, Summer)\)'

    # pattern = re.compile(rf'{cc}\s+(.+?)\n([\s\S]+?)\n.*?Credits (\d+) {seasons_parenthesis}', re.MULTILINE)
    # pattern = re.compile(rf'{cc} {description}\s+?{class_type} {seasons_parenthesis}')
    pattern = re.compile(rf'{full}')
    matches = re.findall(pattern, text)
    return matches

x = read()
print(x)
y = analyze(x)
print()

for i in y:
    print(i[0], i[2:8])
print(len(y))
