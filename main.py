from reader2 import read
import re

class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    def set_next(self, next):
        self.__next = next

    def get_next(self):
        return self.__next
    
    def get_value(self):
        return self.__value

    def __repr__(self) -> str:
        return '(' + str(self.__value) + ' --> ' + str(self.__next) + ')'

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def is_empty(self):
        return self.__head is None

    def __len__(self):
        return self.__size
    
    def __repr__(self) -> str:
        result = ''
        current = self.__head
        while current is not None:
            result += current.get_value()
            current = current.get_next()
        return result
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node
        self.__size += 1


# x = 'test1'
# y = 'test2'
# z = 'test3'

# test = LinkedList()
# test.push(x)
# test.push(y)
# test.push(z)
# print(test)

class Course:
    def __init__(self) -> None:
        self.__code = None
        self.__name = None
        self.__description = None
        self.__prerequisites = None

    def __repr__(self) -> str:
        return f'{self.__code}{self.__name}{self.__description}{self.__prerequisites}'
    
x = Course()
print(x)

