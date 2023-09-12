class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def addLast(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def search(self, key):
        temp = self.head;

        while temp != None:
            if temp.data == key:
                return True
            temp = temp.next

        return False


    def printList(self):
        temp = self.head
        print("The LinkedList Elements Are:")
        
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":

    llist = LinkedList()

    llist.addLast(10)
    llist.addLast(20)
    llist.addLast(30)
    llist.addLast(40)

    print("Searching Element: ",30)
    if llist.search(30):
        print("Search Found")
    else:
        print("Search Not Found")

    print("Searching Element: ",100)
    if llist.search(100):
        print("Search Found")
    else:
        print("Search Not Found") 