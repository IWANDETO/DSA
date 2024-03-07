#!/usr/bin/python3

# This program illustrates how a Queue Data Structure works

class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size


    def enqueue(self, val):
        if self.size == self.rear:
            print("Queue is Full")

        else:
            self.queue[self.rear] = val
            self.rear = self.rear + 1

    def deque(self):
        if self.rear == self.front:
            print("Queue is Empty")

        else:
            print("Dequed Element: ", self.queue[self.front])
            self.front = self.front + 1

if __name__ == "__main__":
    q = Queue(3)

    q.deque()

    print("Adding Element: ", 10)
    q.enqueue(10)

    print("Adding Element: ", 20)
    q.enqueue(20)

    print("Adding Element: ", 30)
    q.enqueue(30)

    print("Adding Element: ", 40)
    q.enqueue(40)

    q.deque()
    q.deque()
    q.deque()
    q.deque()


