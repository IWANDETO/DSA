#!/usr/bin/python3

# This Program illustrates Inorder Traversal of elements(nodes) in a Binary Search Tree

class Node():
    def __init__(self, val): # Constructor to create and initialise nodes
        self.key = val
        self.left = None
        self.right = None

def insert(root, val): # Function used to insert nodes into the BST
    if root == None:  # Function used to insert nodes into the BST
        return Node(val)
    elif root.key > val:  # Function used to insert nodes into the BST
        root.left = insert(root.left, val)
    elif root.key < val: # Check if val is less than root and insert it to the left side of root
        root.right = insert(root.right, val)

    return root # Return root value to the calling function

def inorder(root):
    if root == None:
        return
    
    inorder(root.left)
    print(root.key, end=" ")
    inorder(root.right)

if __name__ == "__main__":
    root = None 

    print("inserting element:", 100)
    root = insert(root, 100) # Insert root element using the Insert function

    print("inserting element:", 50)
    root = insert(root, 50) # Insert elements using the Insert function

    print("inserting element:", 150)
    root = insert(root, 150)

    print("inserting element:", 125)
    root = insert(root, 125)

    print("inserting element:", 300)
    root = insert(root, 300)

    print("The Elements in the Binary Search Tree in Order are: ")
    inorder(root) # Print the elements in the BST in order