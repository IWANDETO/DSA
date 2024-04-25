#!/usr/bin/python3

# This program illustrates searching of Nodes in a Binary Search Tree

class Node():
    def __init__(self, val): # Constructor to create and initialise nodes
        self.key = val
        self.left = None
        self.right = None

def insert(root, val): # Function used to insert nodes into the BST
    if root == None:  # Function used to insert nodes into the BST
        return Node(val)
    elif root.key < val:  # Function used to insert nodes into the BST
        root.right = insert(root.right, val)
    elif root.key > val: # Check if val is less than root and insert it to the left side of root
        root.left = insert(root.left, val)

    return root # Return root value to the calling function

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.key, end=" ")
    inorder(root.right)

def search(root, skey):
    if root == None:
        return False
    if root.key == skey:
        return True
    if root.key < skey:
       return search(root.right, skey)
    else:
       return  search(root.left, skey)



if __name__ == "__main__":

    root = None

    print("Inserting Element: ", 80)
    root = insert(root, 80) # Insert root element using the Insert function

    print("Inserting Element: ", 20)
    root = insert(root, 20) # Insert elements using the Insert function

    print("Inserting Element: ", 100)
    root = insert(root, 100)

    print("Inserting Element: ", 50)
    root = insert(root, 50)

    print("Inserting Element: ", 200)
    root = insert(root, 200)

    print("Inserting Element: ", 300)
    root = insert(root, 300)

    print("Inserting Element: ", 125)
    root = insert(root, 125)

print()
print("The Elements in the Binary Search Tree in order are: ")
inorder(root) # Print the elements in the BST in order

print()
print("Searching Element 20: ")
if search(root, 20) == True:
    print("Search Found")
else:
    print("Search not Found")

print("Searching Element 80: ")
if search(root, 80) == True:
    print("Search Found")
else:
    print("Search not Found")

print("Searching Element 125: ")
if search(root, 125) == True:
    print("Search Found")
else:
    print("Search not Found")

print("Searching Element 500: ")
if search(root, 500) == True:
    print("Search Found")
else:
    print("Search not Found")