#!/usr/bin/python3
#This file demonstrates adding a node to the beginning of a linked last

#We create a class that will create and initialize nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addFirst(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        temp = self.head
        print("The elements in the list are:")

        while (temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':

    llist = LinkedList()

    print("Insering Element: 10")
    llist.addFirst(10)

    print("Insering Element: 20")
    llist.addFirst(20)

    print("Insering Element: 30")
    llist.addFirst(30)

    llist.printList()

