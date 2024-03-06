#!/usr/bin/python3

# This program illustrates how the Stack Data Structure works

class Stack:
    def __innit__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def push(self, val):
        if self.top == self.size -1:
            print("Stack is Full")

        else:
            self.top = self.top + 1
            self.stack[self.top] = val

    def pop(self):
        if self.top == -1:
            print("Stack is Empty")

        else:
            print("Popped Element:", self.stack[self.top])
            self.top = self.top -1

if __name__ == "__main__":
    s = Stack()


    s.pop()

    print("Pushing Element: ", 10)
    s.push(10)

    print("Pushing Element: ", 20)
    s.push(20)

    print("Pushing Element: ", 30)
    s.push(30)

    s.pop()
    s.pop()
    s.pop()