#!/usr/bin/python3

# This program illustrates searching of a Node in a Circular Linked List

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
    
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            
            if temp == self.head:
                break

    def addlast(self, val):
        newNode = Node(val)

        if self.head == None:
            newNode.next = newNode
            self.head = newNode

        else:
            last = self.head

            while last.next != self.head:
                last = last.next

            last.next = newNode
            newNode.next = self.head
    


    def search(self, key):
        if self.head == None:
            return False
        
        temp = self.head

        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp.next == self.head:
                break

            return False

        

if __name__ == "__main__":

    cllist = CircularLinkedList()

    print("Adding Element 10 to the list: ")
    cllist.addlast(10)

    print("Adding Element 20 to the list: ")
    cllist.addlast(20)

    print("Adding Element 30 to the list: ")
    cllist.addlast(30)

    if cllist.search(10) == True:
        print("Search Found")
    else:
        print("Search Not Found")

    if cllist.search(50) == True:
        print("Search Found")
    else:
        print("Search Not Found")

    cllist.printlist()



