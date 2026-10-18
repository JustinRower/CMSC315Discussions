"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

"""
I took a liberty to change the ParentClass and ChildClass names
I chose 'Weapon' and 'Melee' because I've always wondered if
inheritance and polymorphism was how RPGs handled all of the
different weapon types.
""" 


class Weapon:
    # Class variable
    DEFAULT_ICON = "sword.png" # To imitate a placeholder inventory icon
    
    # Constructor
    def __init__(self, name: str, lvl: int):
        self.name = name
        self.lvl = lvl
        
    # Display info
    def display_info(self):
        print(f"Name: {self.name}, Level: {self.lvl}")
        
    # Method for demonstrating inheritance
    def demo_inheritance(self):
        print("This method exists in the Weapon class")


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Melee(Weapon):
    # Class variable
    DEFAULT_RARITY = 'Common'
    
    # Constructor with added 'rarity' and 'dmg' fields
    def __init__(self, name: str, lvl: int, rarity: str, dmg: int):
        super().__init__(name, lvl)
        self.rarity = rarity
        self.dmg = dmg
        
    # Method that swings the melee weapon
    def swing(self):
        print(f"Whoosh! {self.name} does {self.dmg} to enemy!")
        
    # Override from parent class
    def display_info(self):
        print(f"Name: {self.name}, Damage: {self.dmg}, Rarity: {self.rarity}, Level Requirement: {self.lvl}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    # Create two child objects
    sword = Melee('Iron Sword', 2, 'Common', 15)
    hammer = Melee('Adamant Warhammer', 25, 'Rare', 68)
    
    # Display DEFAULT_RARITY through class itself
    print(f"Class variable from class: {Melee.DEFAULT_RARITY}")
    # Display DEFAULT_RARITY through sword object
    print(f"Class variable from object: {sword.DEFAULT_RARITY}")
    
    # Add new attribute to existing object
    hammer.class_req = "Paladin"
    print(hammer.class_req)
    
    # Display namespaces through __dict__
    print(f"Sword namespace:\n{sword.__dict__}")
    print(f"Hammer namespace:\n{hammer.__dict__}")
    
    # Display information about class namespace
    print("Weapon class namespace")
    for key, value in Weapon.__dict__.items():
        # Skip over dunder attributes
        if key.startswith('__'):
            continue
        # Determine if key is method or class variable
        kind = 'method' if callable(value) else 'class variable'
        print(f"{key} ({kind}): {value}")
        
    print("Melee class namespace")
    for key, value in Melee.__dict__.items():
        # Skip over dunder attributes
        if key.startswith('__'):
            continue
        # Determine if key is method or class variable
        kind = 'method' if callable(value) else 'class variable'
        print(f"{key} ({kind}): {value}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    # I will use the same hammer Melee object to demonstrate the copying
    hammer = Melee('Adamant Warhammer', 25, 'Rare', 68)
    # Add nested mutable attribute
    hammer.classes = ['Paladin', 'Warrior']
    
    # Make a shallow copy
    hammer_shallow = copy(hammer)
    # Deep copy
    hammer_deep = deepcopy(hammer)
    
    # Modify the original nested data
    hammer.classes.append('Holy Knight')
    
    # Display the different objects
    # Since classes is an added attribute, I can only display that data
    print(f"Original object classes list: {hammer.classes}")
    print(f"Shallow copy classes list: {hammer_shallow.classes}")
    print(f"Deep copy classes list: {hammer_deep.classes}")

    """
    The difference between a deep and shallow copy is how the original data is
    stored in either copy. In a shallow copy, a new outer object is created
    that copies references to every attribute. This means that providing a new
    object to point an attribute to in a shallow copy will not change the original,
    but updating an existing mutable object that both reference will change both.
    For example, calling shallow.name = new_name points only the copy at a new
    string object, but modifying a list that both obj and shallow reference will
    change the list in both because a new list is not being created; calling
    shallow.list = [new list] would separate the list reference from the original,
    allowing for the modification of it without updating the original list. Deep
    copies are more straight forward. An entirely new object is created, with copies
    of all the attributes and nested objects from the original.
    Because the deep copy shares no references with the original, data can be modified
    safely without modifying the original.
    """

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Parent class
    weapon = Weapon('Sword', 10)
    # Child class
    melee = Melee('Hammer', 5, 'Common', 15)
    
    # Demonstrate inheritance
    weapon.display_info() # Parent version of display_info()
    melee.display_info() # Overridden version in subclass
    melee.demo_inheritance() # Call inherited superclass method from subclass
    melee.swing() # Call subclass exclusive method
    # Show swing() does not exist in Weapon class
    # Attribute error should be thrown
    try:
        weapon.swing()
    except AttributeError as e:
        print(f"Error: {e}")
        

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()