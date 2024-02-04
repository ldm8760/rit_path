import PyPDF2
import re

def read():
    reader = PyPDF2.PdfReader('./Undergrad_Course_Descriptions.pdf')
    page_text = reader.pages[112].extract_text()
    modified_string = page_text.replace('\n', ' ')
    return modified_string

x = read()
print(x)
# well well well
# (\w+-\d+) ([\w\s]+) (Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind Study|CO OP)(?:\s(\d))?.*?Credits (\d|\d - \d) \((Fall|Spring|Summmer|Fall, Spring|Spring, Summer|Fall, Spring, Summer)\)

def analyze(text):
    cc = '(\w+-\d+)'
    description = '([\w\W\s]+?)'
    class_type = '(Lecture|Lab|Recitation|Seminar|Lec\/Lab|Ind Study|CO OP)(?:\s(\d))?.{0,2}Credits (\d|\d - \d)'
    seasons_parenthesis = '\((Fall|Spring|Summmer|Fall, Spring|Spring, Summer|Fall, Spring, Summer)\)'

    # pattern = re.compile(rf'{cc}\s+(.+?)\n([\s\S]+?)\n.*?Credits (\d+) {seasons_parenthesis}', re.MULTILINE)
    pattern = re.compile(rf'{cc} {description}\s+?{class_type} {seasons_parenthesis}')
    matches = re.findall(pattern, text)
    return matches


y = analyze(x)
print()
print()
print()

for i in y:
    print(i)
print(len(y))

text = "Robotics and Manufacturing Engineering Technology RMET-105 Machine Tools Lab Proficiency with traditional machine shop tools will be demonstrated with an emphasis on safety. Students will demonstrate their abilities to interpret drawings and select the appropriate equipment needed to produce each part. Parts built will be inspected by the student to verify the meeting of part requirements. Students will repair/replace any parts that are found to be out of specifications. Inspection tools will be utilized in the product validation requirement of the course. Topics will be experimentally validated through the creation of mechanical parts that will be assembled into a final product. (This class is restricted to MCET-BS or MECA-BS or RMET-BS or EMET-BS major students.)  Lab 2, Credits 1 (Fall, Spring)"
