import re
from MatchMaker import MatchMaker

class University:
    def __init__(self) -> None:
        self.__courseDict: dict[str, Course] = dict()

    def __repr__(self) -> str:
        result = ""
        for value in self.__courseDict.values():
            result += f"{value}\n\n"
        return result

    def addCourse(self, course: 'Course') -> None:
        self.__courseDict[course.getCode()] = course

    def getCourse(self, code: str) -> 'Course':
        return self.__courseDict.get(code) # type: ignore
    
    def printAll(self) -> None:
        courselist = [course for course, info in self.__courseDict.items()]
        print(courselist)


# code-123
# Course title
# Description

class Course:
    def __init__(self, code: str):
        self.__code: str = code

    def format_to_course(self, title: str, description: str, classType1Hours: dict[str, int], 
                 classType2Hours: dict[str, int] = {}, credits: str = "3", season: str = "Fall") -> None:
        
        self.__title: str = title
        self.__description: str = description
        self.__prerequisites: tuple = tuple()
        self.__classType1Hours: dict[str, int] = classType1Hours
        self.__classType2Hours: dict[str, int] = classType2Hours
        self.__credits: int = int(credits)
        self.__season: str = season
        # self.setPrerequisites()

    def __repr__(self) -> str:
        repr_string = (
            f"Code: {self.__code}\n"
            f"Title: {self.__title}\n"
            f"Description: {self.__description}\n"
            f"Prerequisites: {self.__prerequisites}\n"
            f"Class 1 [ClassType, Hours]: {self.__classType1Hours}\n"
            f"Class 2 [ClassType, Hours]: {self.__classType2Hours}\n"
            f"Credits: {self.__credits}\n"
            f"Season(s): {self.__season}"
        )
        return repr_string
    
    def setPrerequisites(self, uni: 'University') -> None:
        desc = self.getDescription()
        valid_text_finder = re.compile(r'(\(Prerequisites:.*)')
        valid_text = re.search(valid_text_finder, desc)
        if valid_text:
            valid_text = valid_text.group(0)
            valid_text.replace("Prerequisites:", "")
            self.__setPrereqHelper(valid_text)        
        else:
            pass

    def __setPrereqHelper(self, text) -> str|None:
        and_condition = [cond.strip() for cond in re.split(r'\band\b', text)]
        or_condition = [cond.strip() for cond in re.split(r'\bor\b', text)]
        print(and_condition)
        print(or_condition)

    # Getter methods
    def getCode(self) -> str:
        return self.__code

    def getTitle(self) -> str:
        return self.__title

    def getDescription(self) -> str:
        return self.__description
    
    # def getPreRequisites(self) -> set['Course']:
    #     return self.__prerequisites

    # def addPreRequisite(self, other: 'Course') -> None:
    #     self.__prerequisites.add(other)

    # def removePreRequisite(self, other: 'Course') -> None:
    #     self.__prerequisites.remove(other)

    def hasPrerequisite(self, other: 'Course') -> bool:
        return self.__prerequisites.__contains__(other)
    
def main():
    matches = MatchMaker()
    text_courses = matches.readFile()
    uni = University()

    for tc in text_courses:
        course = Course(tc[0])
        course.format_to_course(tc[1], tc[2], {tc[3]: int(tc[4]) if len(tc[4]) > 0 else 0}, {tc[5]: int(tc[6]) if len(tc[6]) > 0 else 0}, tc[7], tc[8])
        uni.addCourse(course)

    course1 = uni.getCourse("ACCT-210")
    course1.setPrerequisites(uni)
    # print(course1)
    uni.printAll()

if __name__ == "__main__":
    main()
    

    



    
