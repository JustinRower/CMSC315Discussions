"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


import math
import random
import time


def linear_search(lst, target):
    """
    A linear search has an O(n) time complexity because it scales 
    linearly with the size of the input.
    """
    for i, value in enumerate(lst):
        if value == target:
            return i
    return -1


def binary_search(lst, target):
    """
    Each iteration of the binary search reduces the search space by half
    because each comparison eliminates half of the possible elements.
    """
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(f"Dataset: {small}")

    # Value that exists (23 is at index 5): both searches return 5.
    # Linear search checks 2, 5, 8, 12, 16, 23 (6 comparisons); binary
    # search checks 16, then 56, then 23 (3 comparisons).
    print(f"Search for 23 (exists)   -> linear: {linear_search(small, 23)}, "
          f"binary: {binary_search(small, 23)}")

    # Value that does not exist: both return -1. Linear search had to look at
    # every element to be sure; binary search narrowed the range until it was
    # empty (about log2(10) ~ 4 steps).
    print(f"Search for 40 (missing)  -> linear: {linear_search(small, 40)}, "
          f"binary: {binary_search(small, 40)}")

    # On 10 elements the difference is negligible, so both are effectively
    # instant. The gap only shows up as the dataset grows.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    n = 5000000
    large = list(range(0, n * 2, 2))  # sorted even numbers: 0, 2, ..., 9,999,998
    print(f"Dataset size: {n:,} elements")

    # Worst-ish cases: a value near the end, and a value that is missing.
    # Linear search must scan almost everything (~n comparisons), while binary
    # search needs at most ~log2(n) comparisons.
    for label, target in [("near the end", large[-1]), ("missing", 7)]:
        start = time.perf_counter()
        lin_result = linear_search(large, target)
        lin_time = time.perf_counter() - start

        start = time.perf_counter()
        bin_result = binary_search(large, target)
        bin_time = time.perf_counter() - start

        print(f"Target {target:,} ({label}):")
        print(f"  linear: index {lin_result}, {lin_time * 1000:.3f} ms")
        print(f"  binary: index {bin_result}, {bin_time * 1000:.3f} ms")

    # Both algorithms return the same answers, but binary search is
    # dramatically faster. Each binary step halves the remaining range, so
    # 5,000,000 elements need at most ~23 steps (log2(5,000,000) ~ 22.3),
    # while linear search may need up to 5,000,000. Doubling the data adds
    # just ONE more step for binary search (O(log n)) but doubles the work
    # for linear search (O(n)), so the advantage grows with dataset size.
    # (Binary search requires the data to be sorted.)
    print(f"Max binary search steps for n={n:,}: ~{math.ceil(math.log2(n))}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: empty list. The loop condition (low=0 <= high=-1) is false
    # immediately, so binary search returns -1 without indexing the list.
    print(f"Empty list, search 5      -> linear: {linear_search([], 5)}, "
          f"binary: {binary_search([], 5)}")

    # Edge case 2: single-element list, target present and absent.
    print(f"[7], search 7 (present)   -> linear: {linear_search([7], 7)}, "
          f"binary: {binary_search([7], 7)}")
    print(f"[7], search 3 (absent)    -> linear: {linear_search([7], 3)}, "
          f"binary: {binary_search([7], 3)}")

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================
    #
    # A university registrar keeps student records sorted by student ID and
    # needs to look up students by ID (for example, when they log in to the
    # portal or register for a class). Many lookups happen against the same
    # data, so the cost of each search really adds up.

    print("\n=== REAL-WORLD SCENARIO: STUDENT ID LOOKUP ===")
    random.seed(315)  # fixed seed so results are repeatable
    student_ids = sorted(random.sample(range(1000000, 10000000), 100000))
    records = [{"id": sid, "name": f"Student {sid}"} for sid in student_ids]
    print(f"Registrar database: {len(records):,} student records, sorted by ID")

    # The search functions compare plain values, so we search the sorted list
    # of IDs and use the index that comes back to fetch the full record.
    lookup_id = student_ids[73421]
    index = binary_search(student_ids, lookup_id)
    print(f"Lookup ID {lookup_id} -> record: {records[index]}")

    missing_id = 1  # no student has this ID
    print(f"Lookup ID {missing_id} -> index: {binary_search(student_ids, missing_id)} "
          "(no such student)")

    # Simulate a busy period: 500 lookups, mostly for valid IDs plus a few
    # invalid ones (typos at login).
    requests = random.sample(student_ids, 495) + [1, 2, 3, 4, 5]

    start = time.perf_counter()
    linear_hits = sum(linear_search(student_ids, r) != -1 for r in requests)
    linear_total = time.perf_counter() - start

    start = time.perf_counter()
    binary_hits = sum(binary_search(student_ids, r) != -1 for r in requests)
    binary_total = time.perf_counter() - start

    print(f"{len(requests)} lookups:")
    print(f"  linear: {linear_hits} found, {linear_total * 1000:.1f} ms total")
    print(f"  binary: {binary_hits} found, {binary_total * 1000:.1f} ms total")

    # Both approaches find the same students, but binary search handles the
    # whole batch in a tiny fraction of the time, which is why real systems
    # (databases, indexes, sorted lookup tables) rely on binary-search-style
    # lookups. However, binary search needs the data to be sorted first,
    # and keeping it sorted costs extra whenever records are added. If the
    # data were small, unsorted, or only searched once, linear search would
    # be the simpler and perfectly reasonable choice.


if __name__ == "__main__":
    main()