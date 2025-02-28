import re

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


class TemporaryPrereqs:
    def __init__(self) -> None:
        self.__course: Course
        self.__tempCourse: dict[str, list[str]] = {}

    def addTempPreReq(self, course: 'Course') -> None:
        self.__course = course
        self.__tempCourse[self.__course.getCode()] = self.__setTempPrerequisites()

    def __repr__(self) -> str:
        res = ""
        for key, value in self.__tempCourse.items():
            res += f'{key}, {value}\n'
        return res
    
    def getTemps(self) -> dict[str, list[str]]:
        return self.__tempCourse

    def __setTempPrerequisites(self) -> list[str]:
        res = []
        desc = self.__course.getDescription()
        pattern = re.compile(r'(\w{4}-\d+)')
        matches = re.findall(pattern, desc)
        for tempCourse in matches:
            res.append(tempCourse)
        return res

def matchToCourse(match: tuple) -> 'Course':
    newCourse = Course(match[0], match[1], match[2], {match[3]: int(match[4])}, {match[5]: int(match[6])}, match[7], match[8])
    return newCourse


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
    
    def to_dict(self) -> dict:
        return {
            "code": self.__code,
            "title": self.__title,
            "description": self.__description,
            "prerequisites": [course.to_dict() for course in self.__prerequisites],
            "classType1Hours": self.__classType1Hours,
            "classType2Hours": self.__classType2Hours,
            "credits": self.__credits,
            "season": self.__season
        }

    def writeCourses(self) -> None:
        pass

    def setPrerequisites(self) -> None:
        desc = self.getDescription()
        pattern = re.compile(r'(\w{4}-\d+)')
        matches = re.findall(pattern, desc)
        # for course in matches:
        #     prereq = self.__rit.getCourse(course)
        #     self.addPreRequisite(prereq)

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
    print("Testing")
    uni = University()
    # test1 = matchToCourse()

if __name__ == "__main__":
    main()
    

    



    
