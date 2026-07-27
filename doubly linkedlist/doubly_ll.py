
"""
class Node:
    def __init__(self, data):
        self.data = data 
        self.prev = None 
        self.next = None 

head = Node(10)
head.prev = None 
head.next = Node(20)
head.next.prev = head 
head.next.next = Node(30)
head.next.next.prev = head.next 
head.next.next.next = None 
"""

class Node:
    def __init__(self, data):
        self.data = data 
        self.prev = None 
        self.next = None

head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head 
temp1.next = temp2
temp2.prev = temp1

