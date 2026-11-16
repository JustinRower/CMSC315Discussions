# Unit 5 Discussion: Search Algorithms

## Overview

This project implements and compares two search algorithms, linear search and binary search, in `unit5_discussion.py`.

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Running the Program

```
python unit5_discussion.py
```

## Implementation

### Linear Search

`linear_search(lst, target)` checks each element in order until it finds the target. It returns the index of the match, or `-1` if the target isn't in the list. It works on any list, sorted or not, and takes O(n) time because the work grows with the size of the list.

### Binary Search

`binary_search(lst, target)` works on a sorted list. It tracks a `low` and `high` index and repeatedly checks the middle element:

- If the middle element equals the target, it returns that index.
- If the middle element is smaller than the target, it continues in the upper half.
- If the middle element is larger than the target, it continues in the lower half.

Each step halves the remaining search range, so it takes O(log n) time. If the range becomes empty, the target isn't present and it returns `-1`. Using index bounds instead of slicing avoids copying the list on every step and keeps the returned index correct.

## What `main()` Does

1. **Small dataset test:** searches a 10-element sorted list for a value that exists and one that doesn't, using both algorithms.
2. **Large dataset test:** builds a sorted list with millions of elements and times both algorithms on a value near the end and a missing value. Comments explain why binary search pulls ahead as the data grows.
3. **Edge case tests:** runs both algorithms on an empty list and a single-element list, with the target present and absent.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.
