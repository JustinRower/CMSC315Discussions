"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert the value at the specified index.
    # Every existing element at or after the index is shifted one position to
    # the right to make room for the new value. If the index is greater than
    # the length of the list, the value is simply appended to the end.
    #
    # Performance depends on where the insertion occurs:
    # - Beginning: O(n), because every element has to shift (worst case).
    # - Middle: O(n), because about half the elements have to shift.
    # - End: O(1) amortized, because nothing shifts. The list only occasionally
    #   needs to be resized (copied to a larger block of memory), so the cost
    #   averages out to constant time per append.
    # Extra space used is O(1), aside from the occasional resize.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Validating the index and deleting safely are important for correct behavior.
    # In Python the interpreter handles memory, so an invalid index cannot corrupt
    # memory like it could in C; instead it raises an IndexError that would crash
    # the program if unhandled. Checking first lets us fail gracefully by
    # returning None. Safe deletion also helps avoid logic bugs, such as deleting
    # from an empty list or deleting while iterating (the remaining elements
    # shift left, so the loop would skip one).
    #
    # Valid indices are 0 to len(lst) - 1, or -1 to -len(lst) (negative indices
    # count from the end of the list).
    if not -len(lst) <= index < len(lst):
        return None

    # pop() removes the element and returns it; the elements after it shift left
    # to fill the gap, so deleting from the middle or beginning is O(n).
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a sequential scan because the for loop (with enumerate) visits the
    # elements in order, from index 0 onward. A list is unsorted, so there is no
    # way to rule out a position without looking at it; the only guaranteed way
    # to find the value (or prove it is missing) is to check each element one by one.
    # It stops early and returns the index of the first match.
    #
    # It is a linear search because the time complexity is O(n): doubling the
    # list size doubles the potential number of comparisons.
    for i, item in enumerate(lst):
        if item == value:
            return i

    # The loop finished without finding the value.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    lst = [2, 4]
    print("Original list:", lst)
    insert_at(lst, 0, 1) # Shifts 2, 4 to the right to make room for 1
    print("List after inserting 1 at index 0:", lst)
    insert_at(lst, 2, 3) # Shifts 4 to the right to make room for 3
    print("List after inserting 3 at index 2:", lst)
    insert_at(lst, 4, 5) # Appends 5 to the end of the list
    print("List after inserting 5 at index 4:", lst)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    removed = delete_at(lst, 0) # Removes 1 from the beginning of the list
    print("Removed:", removed, "| list after deleting from the beginning:", lst) # 1 is removed and 2, 3, 4, 5 are shifted to the left
    removed = delete_at(lst, 1) # Removes 3 from the middle of the list
    print("Removed:", removed, "| list after deleting from the middle:", lst) # 3 is removed and 4, 5 are shifted to the left
    removed = delete_at(lst, 2) # Removes 5 from the end of the list
    print("Removed:", removed, "| list after deleting from the end:", lst) # 5 is removed from the end of the list

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("Searching for 2:", search_value(lst, 2)) # Returns 0 because 2 is the first element in the list
    print("Searching for 3:", search_value(lst, 3)) # Returns -1 because 3 is not in the list

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: insert into an empty list
    # There is nothing to shift, so the value simply becomes the only element.
    empty = []
    insert_at(empty, 0, 99)
    print("Insert 99 into empty list at index 0:", empty)  # [99]

    # Edge case 2: insert at an index beyond the end of the list
    # list.insert() does not raise an error; it clamps the index and appends.
    # The value lands at index 3 (the end), not at index 10, and no gap is created.
    short = [1, 2, 3]
    insert_at(short, 10, 4)
    print("Insert 4 at out-of-range index 10:", short)  # [1, 2, 3, 4]
    
    print("\n=== REAL WORLD SCENARIO ===")
    # Real world scenario: Playlist management
    # Say I have a playlist of songs:
    playlist = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5"]
    print("Original playlist:", playlist)
    # I want to add a new song to the beginning of the playlist
    insert_at(playlist, 0, "Song 6")
    print("Playlist after adding Song 6 to the beginning:", playlist)
    # I want to remove the last song from the playlist
    removed = delete_at(playlist, -1)
    print("Removed:", removed, "| playlist after deleting the last song:", playlist)
    # Or, find a song by name and remove it
    # search_value returns -1 when the song is not found, but delete_at treats -1
    # as a valid index (the last element), so check the result before deleting.
    index = search_value(playlist, "Song 3")
    if index != -1:
        removed = delete_at(playlist, index)
        print("Removed:", removed, "| playlist after deleting Song 3:", playlist)
    else:
        print("Song 3 not found, nothing removed")




if __name__ == "__main__":
    main()