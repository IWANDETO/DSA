#!/usr/bin/python3

# This program illustrates deleting a node in a Binary Search Tree

class Node():
    def __init__(self, val): # Constructor to create and initialise nodes
        self.key = val
        self.left = None
        self.right = None

def insert(root, val): # Function used to insert nodes into the BST
    if root == None: # Function used to insert nodes into the BST
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


def deleteNode(root, val):
    if root == None: #Check if BST is empty
        return None    
    elif root.key < val:
        root.right = deleteNode(root.right, val)
    elif root.key > val:
        root.left = deleteNode(root.left, val)
    else:
        if root.left and root.right == None:
            return None
        elif root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            rightMin = getRightMin(root)
            root.key = rightMin
            root.right = deleteNode(root.right, rightMin)

    return root # Return root value to the calling function



def getRightMin(root): #Function to traverse and get the node in the furthest left position of the right child for a case where node to be deleted has two children
    temp = root # Create a temporary variable to hold the furthest left node found

    while temp.left != None:
        temp = temp.left

    return temp.key # Return the value of the furthest left node



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

print("Deleting Element: ", 50)
root = deleteNode(root, 50)

print("Deleting Element: ", 300)
root = deleteNode(root, 300)

print()
print("The Elements in the Binary Search Tree after deletion are: ")
inorder(root) # Print the elements in the BST in order