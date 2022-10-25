from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    data: Any
    next: Any = None

class LinkedList:

    def __init__(self) -> None:
        self.__head = None

    def add_data_at_start(self, data: Any) -> None:

        self.__node = Node(data)
        self.__node.next = self.__head
        self.__head = self.__node

    def display(self) -> None:

        if self.__head == None:
            print("List is Empty")
            return
        
        self.__cur = self.__head
        while self.__cur != None:
            if self.__cur.next == None:
                print(f"[ {self.__cur.data} ]")
            else:
                print(f"[ {self.__cur.data} ]-->", end="")

            self.__cur = self.__cur.next

if __name__ == "__main__":
    l = LinkedList()
    l.add_data_at_start(1)
    l.add_data_at_start(2)
    l.display()