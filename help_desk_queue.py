# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue (self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        removed = self.front
        self.front = removed.next
        if self.front is None:
            self.rear = None
        return removed.value

    def peek(self):
        if self.front is None:
            return None
        return self.front.value

    def print_queue(self):
        if self.front is None:
            print("The queue is empty")
            return
        current = self.front
        postition = 1
        while current is not None:
            print(f"{postition}. {current.value}")
            current = current.next
            postition += 1

    
    


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()
    

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            customer = queue.dequeue()
            if customer is None:
                print("No customers waiting.")
            else:
                print(f"{customer} has been helped.")



        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            customer = queue.peek()
            if customer is None:
                print("No customers waiting.")
            else:
                print(f"Next customer: {customer}")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
