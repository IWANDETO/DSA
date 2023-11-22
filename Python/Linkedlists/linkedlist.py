#!/usr/bin/python3
# This Program will create a linked list in Python 

class Node(): # Create a class to create the node objects
    def __init__(self, data): # Constructor to Initialize the class
        self.data = data
        self.next = None

class LinkedList(): # Create a class to store the node objects
    def __init__(self): 
        self.head = None

    def printList(self): # Create a Method to iterate through the LinkedList and print out node data to the terminal
        temp = self.head # Assign the value of head to a temporary variable

        # Iterate through the list using a while loop
        while temp: # Check if node objects in the linkedlist are still present
            print(temp.data, end=" " )
            temp = temp.next # Assign temp to the next node object

if __name__ == "__main__":
    llist = LinkedList() # Create a LinkedList class object

    # Create Objects of class Node and pass data to the objects
    llist.head = Node(10)
    middle = Node(20)
    last = Node(30)

    # Assign pointers to the linked list(next)
    llist.head.next = middle
    middle.next = last

    print("The Elements in the Linked List are: ")
    llist.printList() # Print out the elements in the LinkedList to the terminal