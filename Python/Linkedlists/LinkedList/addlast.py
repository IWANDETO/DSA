#!/usr/bin/python3

# This is a Python program that inserts a node at the end of a linked list

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    # Add a method that inserts the node at the end of the list
    def addLast(self, val):
        newNode = Node(val)

        if self.head == None: # Assign new node as head of the list if the head node is not present
            self.head = newNode
        else:
            lastNode = self.head # Else assign head to last node

            while lastNode.next != None: # Iterate through the list until the last existing node is found
                lastNode = lastNode.next

            lastNode.next = newNode

    def printList(self):
        temp = self.head
        print("The elements in Linked List are: ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        
if __name__ == "__main__":
    llist = LinkedList()

    print("Adding element 10 to the end of the list")
    llist.addLast(10)

    print("Adding element 20 to the end of the list")
    llist.addLast(20)

    print("Adding element 30 to the end of the list")
    llist.addLast(30)

    llist.printList()


