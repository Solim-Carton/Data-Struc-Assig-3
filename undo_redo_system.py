# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None  # Most recently pushed node
 
    def is_empty(self):
        return self.top is None
 
    def push(self, value):
        """Add new value to top of the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
 
    def pop(self):
        """Remove and return the top value , None if the stack is empty."""
        if self.top is None:
            return None
        removed = self.top
        self.top = removed.next
        return removed.value
 
    def peek(self):
        """Return the top value without removing it ,None if empty."""
        if self.top is None:
            return None
        return self.top.value
 
    def print_stack(self):
        """Print every value in the stack, top to bottom."""
        if self.top is None:
            print("The stack is empty.")
            return
        current = self.top
        while current is not None:
            print(current.value)
            current = current.next

def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack


            print(f"Action performed: {action}")
        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            pass # delete this line
            

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            pass # delete this line


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            
            

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()