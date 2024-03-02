#!/usr/bin/python3

# This program illustrates deleting a Node in a Circular Linked List

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

            if temp.next == self.head:
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

    def delete(self, key):
        if self.head == None:
            return
        
        if self.head.next == self.head and self.head.data == key:
            self.head = None

        elif self.head.data == key:
            lastNode = self.head

            while lastNode.next != self.head: 
                lastNode = lastNode.next

            lastNode.next = self.head.next
            self.head = self.head.next

        else:
            current = self.head
            while current.next != self.head:
                if current.next.data == key:
                    current.next = current.next.next
                    break
                current = current.next 


if __name__ == "__main__":
    cllist = CircularLinkedList()

    print("Adding Element 10 to the list: ")
    cllist.addlast(10)

    print("Adding Element 20 to the list: ")
    cllist.addlast(20)

    print("Adding Element 30 to the list: ")
    cllist.addlast(30)

    print("Adding Element 40 to the list: ")
    cllist.addlast(40)

    print("Adding Element 50 to the list: ")
    cllist.addlast(50)

    cllist.printlist()

    cllist.delete(20)

    cllist.printlist()


