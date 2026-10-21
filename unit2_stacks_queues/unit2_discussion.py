"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
        # This operation supports LIFO behavior because the last item added to the stack is the first item to be removed.

    def pop(self):
        # Empty-stacks should be handled by raising an IndexError.
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
        # Peek returns the top value of the stack without removing it.

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)
        # This operation supports FIFO behavior because the first item added to the queue is the first item to be removed.

    def dequeue(self):
        # Empty-queues should be handled by raising an IndexError.
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def front(self):
        # Front returns the first value of the queue without removing it.
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")
    print("Creating Stack object")
    stack = Stack()
    print("Adding values 1, 2, 3, 4 to stack")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print("Stack: ", stack.items)
    print("Popping value from stack...")
    print(stack.pop())
    print("Stack after popping: ", stack.items)
    print("LIFO behavior: last item (4) is popped first")
    print("Peeking at stack...")
    print(stack.peek())
    print("Stack after peeking: ", stack.items)
    print("LIFO behavior: top value (3) is peeked at")
    print("Creating new empty stack")
    stack = Stack()
    print("Stack is empty: ", stack.is_empty())
    print("Attempting peek on empty stack")
    try:
        stack.peek()
    except IndexError as e:
        print("Expected IndexError: ", e)
    print("Creating new stack with one item")
    stack = Stack()
    stack.push(1)
    print("Stack: ", stack.items)
    print("Popping value from stack")
    print(stack.pop())
    print("Verifying stack is empty: ", stack.is_empty())
    
# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.
    print("\n=== QUEUE DEMO ===")
    print("Creating Queue object")
    queue = Queue()
    print("Adding values 1, 2, 3, 4 to queue")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print("Queue: ", queue.items)
    print("Dequeuing value from queue")
    print(queue.dequeue())
    print("Queue after dequeuing: ", queue.items)
    print("FIFO behavior: first item (1) is dequeued first")
    print("Viewing front of queue")
    print(queue.front())
    print("Attempting dequeue on empty queue")
    try:
        queue.dequeue()
    except IndexError as e:
        print("Expected IndexError: ", e)
    print("Testing front on empty queue")
    queue = Queue()
    try:
        queue.front()
    except IndexError as e:
        print("Expected IndexError: ", e)
    print("Add item to empty queue")
    queue.enqueue(1)
    print("Queue: ", queue.items)
    print("Dequeuing value from queue")
    print(queue.dequeue())
    print("Verifying queue is empty: ", queue.is_empty())

if __name__ == "__main__":
    main()
