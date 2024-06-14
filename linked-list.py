class ListNode:
    def __init__(self, key=None, val=None):
        # Initialize a new node with a key, value, and a pointer to the next node
        self.val = val
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        # Initialize the LinkedList with the head of the list
        self.head = None


    def insert(self, node):
        # Insert a new node at the end of the list
        if not self.head:
            # If the list is empty, set the new node as the head
            self.head = node
        else:
            # Traverse to the end of the list and add the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = node


    def delete(self, key):
        # Delete a node by its key
        current = self.head
        previous = None
        while current:
            if current.key == key:
                # If the node is found, adjust the pointers to remove it from the list
                if previous:
                    # Set the next of the previous node to skip the current node
                    previous.next = current.next
                else:
                    # If the node to be deleted is the head, adjust the head pointer
                    self.head = current.next
                break  # Exit after the first match is found and deleted
            previous = current
            current = current.next



    def search(self, key):
        # Start with the head of the list
        current = self.head
        # Continue searching as long as there are nodes to examine
        while current:
            # Check if the current node's key matches the search key
            if current.key == key:
            # Return the current node if a match is found
                return current
            # Move to the next node in the list
            current = current.next
        # Return None if no node with the given key is found after traversing the entire list
        return None
    

    def replace(self, node, key):
        current = self.head  # Start with the head of the list
        previous = None  # To keep track of the previous node

        while current:
            if current.key == key:
                if previous is None:  # If the node to be replaced is the head
                    self.head = node  # Update the head to the new node
                else:
                    previous.next = node  # Link the previous node to the new node
                node.next = current.next  # Link the new node to the next node in the list
                return  # Assuming we only replace the first occurrence, exit the method
            previous = current  # Move the previous pointer to the current node
            current = current.next  # Move to the next node in the list

