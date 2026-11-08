# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Project Overview

All code is in `unit4_discussion.py`. Run it with `python unit4_discussion.py`.

### `Node`

A single tree node.

- `__init__(value)`: stores the value and sets `left` and `right` to `None`.

### `BST`

A binary search tree that ignores duplicate values.

- `__init__()`: creates an empty tree (`root = None`).
- `insert(value)`: adds a value, creating the root if the tree is empty.
- `_insert_recursive(node, value)`: goes left for smaller values and right for larger values, and creates a node at the first empty spot.
- `search(value)`: returns `True` if the value is in the tree, otherwise `False`.
- `_search_recursive(node, value)`: follows a single path down the tree, going left or right at each node.
- `inorder()`: returns the tree's values as a list.
- `_inorder_recursive(node, values)`: visits left subtree, node, then right subtree, which produces sorted order.

### `main()`

Demonstrates the `BST` class in these sections:

- Tree construction
- In-order traversal
- Search tests
- Edge cases (duplicate values, empty tree)
- Real-world example (student ID lookup)

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.