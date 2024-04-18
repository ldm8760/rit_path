import re
from reader3 import reader3

class University:
    def __init__(self) -> None:
        self.__courseDict: dict[str, Course] = dict()

    def __repr__(self) -> str:
        result = ""
        for key, value in self.__courseDict.items():
            result += f"{key} {value}\n"
        return result

    def addCourse(self, course: 'Course') -> None:
        self.__courseDict[course.getCode()] = course

    def getCourse(self, code: str) -> 'Course':
        return self.__courseDict.get(code) # type: ignore

class Course:
    def __init__(self, code: str, title: str, description: str, classType1Hours: dict[str, int], 
                 classType2Hours: dict[str, int] = {}, credits: str = "3", season: str = "Fall") -> None:
        
        self.__code: str = code
        self.__title: str = title
        self.__description: str = description
        self.__prerequisites: set[Course] = set()
        self.__classType1Hours: dict[str, int] = classType1Hours
        self.__classType2Hours: dict[str, int] = classType2Hours
        self.__credits: int = int(credits)
        self.__season: str = season
        self.__rit: University = University()
        self.setPrerequisites()

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
    
    def setPrerequisites(self) -> None:
        desc = self.getDescription()
        pattern = re.compile(f'(\w{4}-\d+)')
        matches = re.findall(pattern, desc)
        for course in matches:
            prereq = self.__rit.getCourse(course)
            self.addPreRequisite(prereq)

    # Getter methods
    def getCode(self) -> str:
        return self.__code

    def getTitle(self) -> str:
        return self.__title

    def getDescription(self) -> str:
        return self.__description
    
    def getPreRequisites(self) -> set['Course']:
        return self.__prerequisites

    def addPreRequisite(self, other: 'Course') -> None:
        self.__prerequisites.add(other)

    def removePreRequisite(self, other: 'Course') -> None:
        self.__prerequisites.remove(other)

    def hasPrerequisite(self, other: 'Course') -> bool:
        return self.__prerequisites.__contains__(other)
    
def main():
    results = reader3()
    results.read()
    text = results.getContents()
    preCourses = results.analyze(text)
    postCourses = University()
    for course in preCourses:
        postCourses.addCourse(Course(course[0], course[1], course[2], {course[3]: course[4]}, {course[5]: course[6]}, course[7], course[8])) # type: ignore
    print(postCourses)

    
if __name__ == "__main__":
    main()
    

    



    
