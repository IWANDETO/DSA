#!/usr/bin/python3

# This program illustrates Inserting Nodes in a Binary Search Tree

class Node():
    def __init__(self, val): # Method to create and initialise nodes
        self.key = val
        self.left = None
        self.right = None

def insert(root, val): # Function used to insert nodes into the BST
    if root == None: # Check if root is empty, if so assign val to be root
        return Node(val)
    elif root.key < val: # Check if val is greater than root and insert it to the right side of root
        root.right = insert(root.right, val)
    elif root.key > val: # Check if val is less than root and insert it to the left side of root
        root.left = insert(root.left, val)
            
    return root


if __name__ == "__main__":
    root = None

    print("inserting element:", 100)
    root = insert(root, 100)

    print("inserting element:", 50)
    root = insert(root, 50)

    print("inserting element:", 150)
    root = insert(root, 150)

    print("inserting element:", 125)
    root = insert(root, 125)

    print("inserting element:", 300)
    root = insert(root, 300)

