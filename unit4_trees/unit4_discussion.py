"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Initialize the node's value and left and right leaf references
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Initialize the root of the BST
        self.root = None

    def insert(self, value):
        """
        Insertion depends on whether a value is smaller or larger than the current node
        because of the nature of the BST. If the value is smaller, it will be inserted into the left subtree,
        if the value is larger, it will be inserted into the right subtree.
        Duplicate values are ignored (this BST does not store duplicates).
        """
        # If the root is None, create a new node and set it as the root
        if self.root is None:
            self.root = Node(value)
        else:
            # If the root is not None, insert the value recursively
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:            # found an empty leaf
            return Node(value)
        if value < node.value:    # insert into the left subtree
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:    # value is greater than the current node, insert into the right subtree
            node.right = self._insert_recursive(node.right, value)    
        return node

    def search(self, value):
        """
        BST searches are more efficient than linear searches because each comparison
        can eliminate about half of the remaining items to search through. In a 
        reasonably balanced BST, the average search time is O(log n), 
        which is much faster than the O(n) time complexity of a linear search.
        """
        if self.root is None:            # empty tree
            return False
        return self._search_recursive(self.root, value)    # search recursively

    def _search_recursive(self, node, value):
        if node is None:            # found an empty leaf
            return False
        if value == node.value:    # found the value
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        return self._inorder_recursive(self.root, [])

    def _inorder_recursive(self, node, values):
        """
        In-order traversal visits the left subtree, the current node, and the right subtree.
        This produces a sorted output in a BST because the left subtree is always less than the current node,
        and the right subtree is always greater than the current node.
        """
        if node is not None:
            self._inorder_recursive(node.left, values)    # visit the left subtree
            values.append(node.value)
            self._inorder_recursive(node.right, values)    # visit the right subtree
        return values


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        tree.insert(value)
    print(f"Values inserted: {values}")
    # BSTs are efficient at reducing search space for each step because each comparison
    # lets us skip an entire subtree. In a reasonably balanced tree, that eliminates
    # about half of the remaining items at every step.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print(f"In-order traversal: {tree.inorder()}")
    # The traversal produces sorted output because of the BST ordering rule: every value in
    # the left subtree is less than the current node, and every value in the right subtree is
    # greater. Visiting left, then the node, then right therefore yields values in ascending
    # order.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print(f"Searching for 30: {tree.search(30)}")
    print(f"Searching for 50: {tree.search(50)}")
    print(f"Searching for 90: {tree.search(90)}")
    print(f"Searching for 25: {tree.search(25)}")
    # Searching for 30 and 50 return True because they are in the BST.
    # Searching for 90 and 25 return False because they are not in the BST.
    # (e.g. 25 is < 50, < 30, > 20, then hits an empty spot, so the search stops.)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("Duplicate value edge case:")
    # I used a no-duplicate convention for the BST, so duplicate values should be ignored.
    tree = BST()
    values = [50, 30, 80, 30]
    for value in values:
        tree.insert(value)
    print(f"Values inserted: {values}")
    print(f"In-order traversal: {tree.inorder()}")
    # The duplicate value is ignored because it is already in the BST.

    print("\nEmpty tree edge case:")
    empty_tree = BST()
    print(f"In-order traversal of empty tree: {empty_tree.inorder()}")
    print(f"Searching empty tree for 5: {empty_tree.search(5)}")
    # An empty tree has no root, so traversal returns an empty list and search returns False.

    # ===============================
    # REAL-WORLD EXAMPLE: STUDENT ID LOOKUP
    # ===============================
    #
    # A university system can store student ID numbers in a BST. Looking up whether an ID
    # is registered only needs to follow one path from the root down, instead of checking
    # every ID like a linear search would. The in-order traversal also gives an
    # automatically sorted roster of IDs.

    print("\n=== REAL-WORLD EXAMPLE: STUDENT ID LOOKUP ===")
    student_ids = [304512, 287340, 331209, 270118, 296775, 318842, 345601]
    roster = BST()
    for student_id in student_ids:
        roster.insert(student_id)
    print(f"IDs registered (in order entered): {student_ids}")
    print(f"Sorted roster (in-order traversal): {roster.inorder()}")
    print(f"Is 318842 registered? {roster.search(318842)}")
    print(f"Is 300000 registered? {roster.search(300000)}")
    # Finding 318842 takes 3 comparisons (304512 -> 331209 -> 318842) instead of up to 7
    # for a linear search. With millions of students, the gap between O(log n) and O(n)
    # becomes huge, which is why ordered lookups like this use tree structures.



if __name__ == "__main__":
    main()