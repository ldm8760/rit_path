from Course import Course, matchToCourse
import csv

class University:
    def __init__(self) -> None:
        self.__courseDict: dict[str, Course] = dict()

    def __repr__(self) -> str:
        result = ""
        for value in self.__courseDict.values():
            result += f"{value}\n\n"
        return result
    
    def __len__(self) -> int:
        return len(self.__courseDict)

    def addCourse(self, course: 'Course') -> None:
        self.__courseDict[course.getCode()] = course

    def getCourse(self, code: str) -> 'Course':
        return self.__courseDict.get(code) # type: ignore
    
    @classmethod
    def load_courses(cls, filename):
        """Load courses from a CSV file into a University object."""
        uni = cls()
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for course in reader:
                uni.addCourse(matchToCourse(course))
        return uni