#!/usr/bin/python3

# This program creates a double linked list using Python

class Node(): # create a class node to create node objects and initialize them
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList(): # Create a Doubly linked list that stores node objects and initializes them
    def __init__(self):
        self.head = None

    def printList(self): # define a method to print out the elements in the list
        temp = self.head

        print("Forward Traversal:")
        while temp != None:
            print(temp.data)
       
            if temp.next == None: # Check for the last node in the list
                last = temp # Assign a value to last to be used in backward traversal
                break
                
            temp = temp.next

        print("Backward Traversal")
        temp = last
        while temp != None:
            print(temp.data)
            temp = temp.prev

if __name__ == "__main__":

    dllist = DoubleLinkedList()

    dllist.head = Node(10)
    middle = Node(20)
    last = Node(30)

    # Assign nodes prev and next pointers
    dllist.head.prev = None
    dllist.head.next = middle
    middle.prev = dllist.head
    middle.next = last
    last.prev = middle

    dllist.printList()

        
        