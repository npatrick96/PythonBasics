class SinglyLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        
# make a singly linked list that looks like:
# 1 -> 2 -> 3 -> None
# create 3 nodes, then connect them

a  = SinglyLinkedNode(1)
b  = SinglyLinkedNode(2)
c  = SinglyLinkedNode(3)

a.next = b 
b.next = c

class DoublyLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

        
# make a doubly linked list that looks like:
# None <- 9 <--> 0 -> None
      
d = DoublyLinkedNode(9)
e = DoublyLinkedNode(0)


d.next = e
e.previous = d
