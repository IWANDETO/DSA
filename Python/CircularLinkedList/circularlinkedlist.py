#!/usr/bin/python3

# This Program illustrates the Basics of a Circular Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None


    def printList(self):
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        

if __name__ == "__main__":
    dllist = CircularLinkedList()

    dllist.head = Node(10)
    middle = Node(20)
    last = Node(30)

    dllist.head.next = middle
    middle.next = last
    last.next = dllist.head


    print("The Elements in the List are: ")
    dllist.printList()