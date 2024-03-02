#!/usr/bin/python3

# This program illustrates adding a Node at the end of a Circular Linked List

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head

        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break

    def addlast(self, val):
        newNode = Node(val)

        if self.head == None:
            newNode.next = newNode
            self.head = newNode

        else:
            last = self.head

            if last.next != None:
                last = last.next

            last.next = newNode
            newNode.next = self.head


if __name__ == "__main__":

    cllist = CircularLinkedList()

    print("Adding Element 30 to the list: ")
    cllist.addlast(30)

    print("Adding Element 20 to the list: ")
    cllist.addlast(20)

    print("Adding Element 10 to the list: ")
    cllist.addlast(10)

    cllist.printlist()
