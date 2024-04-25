#!/usr/bin/python3

# This program illustrates deleting a node in a Binary Search Tree

class Node():
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None

def insert(root, val):
    if root == None:
        return Node(val)
    elif root.key < val:
        root.right = insert(root.right, val)
    elif root.key > val:
        root.left = insert(root.left, val)

    return root


def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root, end=" ")
    inorder(root.right)

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

