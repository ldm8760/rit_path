from Course import Course
import csv

def matchToCourse(match: dict) -> 'Course':
    newCourse = Course(match["Code"], match["Title"], match["Description"], 
                       {match["Class1Type"]: (int(match["Class1TypeHours"]) if match["Class1TypeHours"] != '' else 0)}, 
                       {match["Class2Type"]: (int(match["Class2TypeHours"]) if match["Class2TypeHours"] != '' else 0)}, 
                       match["Credits"], match["Season"])
    return newCourse

class University:
    def __init__(self) -> None:
        self.__courseDict: dict[str, Course] = dict()

    def __repr__(self) -> str:
        return "\n\n".join(map(str, self.__courseDict.values()))
    
    def __len__(self) -> int:
        return len(self.__courseDict)

    def addCourse(self, course: 'Course') -> None:
        self.__courseDict[course.getCode()] = course

    def getCourse(self, code: str) -> 'Course':
        return self.__courseDict.get(code) # type: ignore
    
    def findSubject(self, subject: str) -> list[str]:
        subject = subject.upper()
        return [key for key in self.__courseDict.keys() if key.startswith(subject)]
    
    @classmethod
    def load_courses(cls, filename):
        """Load courses from a CSV file into a University object."""
        uni = cls()
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for course in reader:
                uni.addCourse(matchToCourse(course))
        return uni