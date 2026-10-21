# Unit 2 Discussion: Stacks and Queues

## Overview

This will provide a brief overview of the functionality of the project.
The implementation process and reflection will be posted to the LEO discussion post.

Use the following to run the program:
`python3 unit2_discussion.py`

## Stack

The Stack class implements a simple stack data structure using a Python list.

Methods:
 - Constructor: initializes the stack object with an empty list
 - push(self, value): Adds value to the top of the stack
 - pop(self): Removes top value from the stack, returns popped value. Raises ValueError if stack is empty
 - peek(self): Returns top value from stack without removing it. Raises ValueError if stack is empty
 - is_empty(self): Returns true if stack is empty, false otherwise

## Queue

The Queue class uses deque from the collections library to make a Queue

Methods:
 - Constructor: intializes Queue with deque()
 - enqueue(self, value): Adds value to the beginning of the Queue
 - dequeue(self): Removes and returns first item in Queue. Raises ValueError if Queue is empty
 - front(self): Returns first item in Queue without removing it. Raises ValueError if Queue is empty
 - is_empty(self): Returns true if Queue is empty, false otherwise.

## Main

Main provides a demonstration of the above classes.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.
