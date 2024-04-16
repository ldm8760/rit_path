import re

class Course:
    def __init__(self, code: str, title: str, description: str, classType1Hours: dict[str, int], classType2Hours=None) -> None:
        self.__code: str = code
        self.__title: str = title
        self.__description: str = description
        self.__prerequisites: set[Course] = set()
        self.__classType1Hours: dict[str, int] = classType1Hours
        self.__classType2Hours: dict[str, int] = classType2Hours if classType2Hours else {}

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
    
    def setPrerequisites(self) -> None:
        desc = self.getDescription()
        pattern = re.compile(f'(\w{4}-\d+)')
        matches = re.findall(pattern, desc)

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
    course = Course("", "", "", {})
    print(course)

if __name__ == "__main__":
    main()


    



    
