import re

class Course:
    def __init__(self, code: str, title: str, description: str, classType1Hours: dict[str, int],
                 classType2Hours: dict[str, int] = {}, credits: str = "3", season: str = "Fall") -> None:
        
        self.__code: str = code
        self.__title: str = title
        self.__description: str = description
        self.__classType1Hours: dict[str, int] = classType1Hours
        self.__classType2Hours: dict[str, int] = classType2Hours
        self.__credits = credits
        self.__season: str = season
        self.__prerequisites: str = self.set_prereqs()


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

    def set_prereqs(self) -> str:
        basic_desc = self.__description.replace("\n", "")
        basic_text = re.search(r'Prerequisites:\s*?([\w\W\s]*)\)', basic_desc)
        if basic_text is not None:
            basic_text = basic_text.group(1)
            basic_text.split(" ")
            print(basic_text)
            return basic_text
        else:
            return ""

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

    # def hasPrerequisite(self, other: 'Course') -> bool:
    #     return self.__prerequisites.__contains__(other)
    

    



    
