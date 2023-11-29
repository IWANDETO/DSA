#!/usr/bin/python3
# This is a python program to demonstrate adding a node object to the beginning of the Linked List

class Node(): # Create a class to create and new node objects
    def __init__(self, data): # Create a Constructor to initialize the class
        self.data = data
        self.next = None

class LinkedList(): # Create a class LinkedList to store the node objects in a linkedlist
    def __init__(self): # Create a Constructor to initialize the class
        self.head = None

    def addFirst(self, val): # Create a method to add a New Node to the beginning of the list
        newNode = Node(val) # New Node creates a Node objects and takes value as an argument
        newNode.next = self.head # Point the new node to the head of the list
        self.head = newNode # Make the new node the head of the lsit

    def printList(self): # Method to iterate through the linkedlist and print out node components
        temp = self.head # Assign the value of head to a temporary variable

        # Iterate through the list using a while loop
        while temp: 
            print(temp.data, end=" ")
            temp = temp.next # Assign temp to the next node in the list

if __name__ == "__main__":
    llist = LinkedList()
    
    print("Adding element 10 to the list: ")
    llist.addFirst(10) # Add a node element to the list
    
    print("Adding element 20 to the list: ")
    llist.addFirst(20)

    print("Adding element 30 to the list: ")
    llist.addFirst(30)

    print("The Elements in the List are: ")
    llist.printList()