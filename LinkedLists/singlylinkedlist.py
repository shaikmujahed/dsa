"""
******Singly linked lists********
"""

class SinglyNode:
    def __init__(self,val,next=None):
        self.val = val 
        self.next = next

    def __str__(self):
        return str(self.val)

head = SinglyNode(1)
a = SinglyNode(3)
b = SinglyNode(4)
c = SinglyNode(7)

head.next = a
a.next = b
b.next = c

#print(head)

# Traverse the list - O(n) time
curr = head
while curr:
    #print("current element: ", curr)
    curr = curr.next

# Display linked list - O(n) time
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements))
#display(head)


# Search operation for a node take - O(n) time
def search(head,val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False
#print(search(head,7))






"""
*****Dubly linked list******
"""


class DublyNode:
    def __init__(self,val,next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

head = tail = DublyNode(1)
#print(tail)
    
# Display operation takes - O(n) time
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(elements))
#display(head)

#Inserting at beginning takes - O(1) time
def insert_at_biginning(head, tail,val):
    new_node = DublyNode(val,next=head)
    #print("Dubly: ",new_node)
    head.prev = new_node
    #print("prev: ", head.prev)
    return new_node, tail

head, tail = insert_at_biginning(head,tail,3)
#display(head)

# Inserting at the end take - O(1)
def insert_at_end(head, tail, val):
    new_node = DublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display(head)

