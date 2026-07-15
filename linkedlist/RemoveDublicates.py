
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


head = Node(10)
head.next = Node(10)
head.next.next = Node(20)
head.next.next.next = Node(30)
head.next.next.next.next = Node(40)
head.next.next.next.next.next = Node(50)


def RemoveDublicates(head):
    curr = head
    while curr and curr.next:
        if curr.key == curr.next.key:
            curr.next = curr.next.next 
        else:
            curr = curr.next 
    return head 


def PrintLinkedList(head):
    curr = head
    while curr:
        print(curr.key, end=" ")
        curr = curr.next


head = RemoveDublicates(head)
PrintLinkedList(head)
