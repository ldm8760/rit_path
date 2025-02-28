import re
import csv

class MatchMaker:
    def __init__(self) -> None:
        self.__FILENAME: str = "test.txt" # 75 courses
        # self.__contents: list[str] = self.readFile()

# if __name__ == "__main__":
#     with open(INPUT_FILE, "r", encoding="utf-8") as file:
#         content = file.read()
#     makeMatches(content)