#!/usr/bin/python3

# This file demonstrates the basics of creating a Node in a Binary Search Tree

class Node():
    def __init__(self, val):
        self.key = val # Key element in a node (value of any data type)
        self.left = None # Left pointer which is none by default
        self.right = None # Right pointer which is none by default

if __name__ == "__main__":

    root = Node(10) # Create a root node and assign the value 10
