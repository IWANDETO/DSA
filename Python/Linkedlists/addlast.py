#!/usr/bin/python3
#This file demonstrates adding a node at the end of a lonked list

#Define class node to create and initialize nodes
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

#Define a new class that holds the head node of the linked list
class LinkedList:
    def __init__ (self):
        self.head = None

#define method that adds a new node 
    def addlast(self, val):
        newNode = Node(val)

        if self.head == None:
            self.head = newNode
        else:
            lastNode = self.head

            while lastNode.next != None:
                lastNode = lastNode.next

            lastNode.next = newNode

    def printList(self):
        temp = self.head
        print("The Elements in the Linked List are: ")

        while (temp):
            print(temp.data, end = " ")
            temp = temp.next

if __name__ == "__main__":
    llist = LinkedList()

    print("Inserting Element: 10")
    llist.addlast(10)
    print("Inserting Element: 20")
    llist.addlast(20)
    print("Inserting Element: 30")
    llist.addlast(30)

    llist.printList()





