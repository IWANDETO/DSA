#!/usr/bin/python3

# This Python programs is used to search if a node element is present in a Linkedlist

class Node(): # Class Node creates a new node object and initializes
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None

    def addfirst(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def search(self, key):
        temp = self.head

        while temp != None:
            if temp.data == key:
                return True
            temp = temp.next 
        return False
    
if __name__ == "__main__":
    llist = LinkedList()
    print("Adding element 10")
    llist.addfirst(10)

    print("Adding element 20")
    llist.addfirst(20)

    print("Adding element 30")
    llist.addfirst(30)

    print("Adding element 40")
    llist.addfirst(40)

    # Search an existing element in the list
    print("Searching for element", 20)
    if llist.search(20):
        print("Search Found")
    else:
        print("Search Not Found")

    # Search an element that is not present in the list
    print("Searching for element", 100)
    if llist.search(100):
        print("Search Found")
    else:
        print("Search Not Found")