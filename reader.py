import re

# with open('Undergrad_Course_Descriptions.txt', "r") as f:
#     for i in range(1000):
#         reader = f.readline()
#         test = re.findall(r'\b[A-Z]+-\d{3}\b', reader)

# text = "The course codes are ABC-123 and CGLS-499."

# course_pattern_with_boundaries = re.findall(r'\b[A-Z]+-\d{3}\b', text)
# print("With Word Boundaries:   ", course_pattern_with_boundaries

# Ideal outcome:
    # Course.__code = 'FINC-220'
    # Course.__description = 'Yata yata'
    # Course.__prerequisites = ['(ECON-101 or ECON-201)' and 'ACCT-110' and '(STAT-145 or STAT-251 or CQAS-251 or MATH-251 or MATH-252 or STAT-205)' or equivalent courses.]        

test_text = "INTB-300 Cross-Cultural Management Description (Prerequisites: INTB-225 or equivalent course.) Lecture 3, Credits 3 (Fall, Spring) INTB-310 Description (Prerequisites: INTB-225 or equivalent course.) Lecture 3, Credits 3 (Biannual) INTB-315 Exporting and Global Sourcing Description (Prerequisites: INTB-225 or equivalent course.) Lecture 3, Credits 3 (Fall, Spring)"

text = "Your text here with cccc-nnn patterns, cccc-111, and also (cccc-nnn) abcd-123."

# course = Course(text).get_code()
# print(course)

text = "INTB-300 Your text here with cccc-123 patterns, (exclude this) cccc-111, and also (also exclude this) (cccc-123)."

pattern = re.compile(r'\([^()]+\)|([^()]+)(.*)')
matches = pattern.findall(text)

print(matches)

