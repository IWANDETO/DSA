#!/usr/bin/python3

# This is a Python Progam that deletes a node from a Linked List

class Node(): # Class creates node objects and initializes
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(): # Class creates a Linkedlist that holds the node objects
    def __init__(self):
        self.head = None

    def addfirst(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def delete(self, key): # Create a method that takes key as argument and used to delete a given element(key)

        if self.head.data == key: # Check if the head node is the key to be deleted
            self.head = self.head.next

        else:
            temp = self.head # Assign head node to a temporary variab

            while temp.next != None:
                if temp.next.data == key:
                    temp.next = temp.next.next
                    break
                else:
                    temp = temp.next

    def printList(self):
        temp = self.head

        print("The Elements in the Linked List are: ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":
    llist = LinkedList()

    print("Adding element 10 to the list")
    llist.addfirst(10)

    print("Adding element 20 to the list")
    llist.addfirst(20)

    print("Adding element 30 to the list")
    llist.addfirst(30)
    
    llist.printList()

    # Delete a Node from the list
    print("Deleting Node 20 from the list")
    llist.delete(20)

    # Print the list elements after deletion
    llist.printList()