
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


def IsSorted(head):
    if head is None or head.next is None:
        return True
    
    curr = head
    while curr.next and curr.key == curr.next.key:
        curr = curr.next 

    if curr.next is None:
        return True
    
    ascending = curr.key < curr.next.key
    while curr.next:
        if ascending:
            if curr.key > curr.next.key:
                return False
        else:
            if curr.key < curr.next.key:
                return True
        curr = curr.next 
    return True

print(IsSorted(head))
