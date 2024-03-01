#!/usr/bin/python3

# This program illustrates deleting a Node in a Circular Linked List

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

            if temp.next == self.head:
                break

    def addlast(self, val):
        newNode = Node(val)
        last = self.head

        if last.next == None:
            last.next = newNode
            self.head = newNode

        else:
            while last.next:
                last = last.next

            last.next = newNode
            newNode.next = self.head

    def delete(self, key):
        temp = Node(key)
        last = self.head

        while last.next != None:
            if last.data == temp.key:
                last.next = last.next.next

if __name__ == "__main__":
    cllist = CircularLinkedList()

    print("Adding Element 10 to the list: ")
    cllist.addlast(10)

    print("Adding Element 20 to the list: ")
    cllist.addlast(20)

    print("Adding Element30 to the list: ")
    cllist.addlast(30)

    cllist.printlist()

    cllist.delete(20)

    cllist.printlist()


