
# nth Node from the end of Linked List

class Node:
    def __init__(self, key):
        self.key = key 
        self.next = None 

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

# 10 -> 20 -> 30 -> 40 -> 50

def nthNode(head,n):
    curr = head
    length = 0
    while curr is not None:
        curr = curr.next 
        length+=1

    curr = head
    for _ in range(0, length - n):
        curr = curr.next 
    print(curr.key)

nthNode(head, 3)
