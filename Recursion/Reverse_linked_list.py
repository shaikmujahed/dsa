# Node class to represent each element of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class to manage the list
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Method to display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the pointer
            prev = current  # Move the previous pointer forward
            current = next_node  # Move to the next node
        self.head = prev  # Update the head to the new front

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    print("Original Linked List:")
    linked_list.display()

    linked_list.reverse()

    print("Reversed Linked List:")
    linked_list.display()
