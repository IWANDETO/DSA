#!/usr/bin/python3

# This Program demonstrates adding of a New Node to the beginning of a Circular linked list

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

    def addfirst(self, val):
        newNode = Node(val)

        if self.head == None:
            newNode.next = newNode
            self.head = newNode

        else:
            lastNode = self.head

            while lastNode.next != self.head:
                lastNode = lastNode.next
            
            lastNode.next = newNode
            newNode.next = self.head
            self.head = newNode
    

if __name__ == "__main__":

    cllist = CircularLinkedList()

    print("Adding Element 10 to the list: ")
    cllist.addfirst(10)

    print("Adding Element 20 to the list: ")
    cllist.addfirst(20)

    print("Adding Element 30 to the list: ")
    cllist.addfirst(30)

    cllist.printlist()





