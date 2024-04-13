

class Course:
    def __init__(self) -> None:
        self.__code : str = ""
        self.__title : str = ""
        self.__description : str = ""
        self.__prerequisites : set[Course] = set()
        self.__classType1Hours : dict[str, int] = dict()
        self.__classType2Hours : dict[str, int] = dict()

    def __repr__(self) -> str:
        repr_string = (
            f"Code: {self.__code}\n"
            f"Title: {self.__title}\n"
            f"Description: {self.__description}\n"
            f"Prerequisites: {self.__prerequisites}\n"
            f"Class 1 [ClassType, Hours]: {self.__classType1Hours}\n"
            f"Class 2 [ClassType, Hours]: {self.__classType2Hours}"
        )
        return repr_string

    # Getter methods
    def getCode(self) -> str:
        return self.__code

    def getTitle(self) -> str:
        return self.__title

    def getDescription(self) -> str:
        return self.__description

    # Setter methods
    def setCode(self, code: str) -> None:
        self.__code = code

    def setTitle(self, title: str) -> None:
        self.__title = title

    def setDescription(self, description: str) -> None:
        self.__description = description
    

    def setClassTypeHours1(self, classTypeAndHours: dict[str, int]) -> None:
        self.__classType1Hours = classTypeAndHours

    def setClassTypeHours2(self, classTypeAndHours: dict[str, int]) -> None:
        self.__classType2Hours = classTypeAndHours
    
    def getPreRequisites(self) -> set['Course']:
        return self.__prerequisites

    def addPreRequisite(self, other: 'Course') -> None:
        self.__prerequisites.add(other)

    def removePreRequisite(self, other: 'Course') -> None:
        self.__prerequisites.remove(other)

    def hasPrerequisite(self, other: 'Course') -> bool:
        return self.__prerequisites.__contains__(other)
    
def main():
    course = Course()
    print()
    course.setCode("TEST-101")
    course.setTitle("INTRO TO TESTING")
    course.setClassTypeHours1({"lecture": 3})
    print(course)

if __name__ == "__main__":
    main()


    



    
