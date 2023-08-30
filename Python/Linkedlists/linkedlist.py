#!/usr/bin/python3
#This file is a demo for Linked Lists using Python

#create a class node that will create and initialize the nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#create a class that will hold the head node of the  linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == '__main__': #checking if the code is run under the main file
    llist = LinkedList() #Create linked list object

    llist.head = Node(10)
    middle = Node(20)
    last = Node(30)

    llist.head.next = middle
    middle.next = last

    print("The LinkedList Elements Are:")
    llist.printList()  # Print the linked list



    







