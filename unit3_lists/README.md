# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.
The program (`unit3_discussion.py`) implements three helper functions and runs
a series of tests that show how each operation behaves, including edge cases.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## How to Run

```
python unit3_discussion.py
```

No external libraries are needed.

## Program Structure

### Functions

| Function | Description | Returns | Time complexity |
|---|---|---|---|
| `insert_at(lst, index, value)` | Inserts `value` at `index` using `list.insert()`. Elements at or after the index shift right. An index past the end appends the value. | Nothing (modifies the list in place) | O(n) at the beginning or middle, O(1) amortized at the end |
| `delete_at(lst, index)` | Validates the index, then removes the element with `list.pop()`. Elements after it shift left. | The removed value, or `None` if the index is invalid | O(n) at the beginning or middle, O(1) at the end |
| `search_value(lst, value)` | Scans the list one element at a time with a `for` loop and `enumerate`. | The index of the first match, or `-1` if not found | O(n) |

Notes:

- `delete_at` treats both `0` to `len(lst) - 1` and `-1` to `-len(lst)` as valid
  indices. Anything else returns `None` without changing the list.
- `search_value` is a linear search: a list is unsorted, so every position may
  need to be checked, and the work grows in proportion to the list size.
- Each function includes comments that explain the behavior and performance.

### Tests in `main()`

1. **Insertion tests:** starts with `[2, 4]`, inserts at the beginning, middle,
   and end, and prints the list after each step.
2. **Deletion tests:** deletes from the beginning, middle, and end, and prints
   both the removed value and the updated list.
3. **Search tests:** searches for a value that exists and one that does not.
4. **Edge cases:**
    - Insert into an empty list
    - Insert at an index beyond the end of the list (the value is appended)
5. **Real-world scenario (playlist management):** starts with a playlist of five
   songs, adds a song to the beginning, removes the last song, and finds a song
   by name before removing it. The search result is checked first, because
   `search_value` returns `-1` for a missing song, and `delete_at` would treat
   `-1` as the last element and delete the wrong song.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?
