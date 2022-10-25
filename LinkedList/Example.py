#Conflict Error
from dataclasses import dataclass, field
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
    
    def add_data_at_end(self, data: Any) -> None:
        self.__node = Node(data)

        if self.__head == None:
            self.head = self.__node
        else:
            self.__cur = self.__head

            while self.__cur.next != None:
                self.__cur = self.__cur.next

            self.__cur.next = self.__node

    def add_data_at_specific_index(self, data: Any, index: int) -> None:

        if index == 0:
            self.add_data_at_start(data)
            return
        if index-1 == 0:
            self.add_data_at_end(data)
            return
        self.node = Node(data)
        count = 0
        self.__cur = self.__head
        try:
            while count != index-1:
                self.__cur = self.__cur.next
                count += 1

            
                self.prv = self.__cur.next
                self.__cur.next = self.node
                self.node.next = self.prv
        except AttributeError:
            print("Index Out Bound")
            exit(0)


    def is_empty(self) -> bool:
        if self.__head == None:
            return True
        return False 

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
    l.add_data_at_start(0)
    l.add_data_at_end(1)
    l.add_data_at_end(2)
    l.add_data_at_end(3)
    l.add_data_at_specific_index(2.5, 2)
    l.display()
    l.add_data_at_specific_index(2.5, 10)
    l.display()
