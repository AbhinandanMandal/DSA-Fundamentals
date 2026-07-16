
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)


def ReverseLinkedList(head):
    curr = head
    key_list = []
    while curr:
        key_list.append(curr.key)
        curr = curr.next
    # key_list = [10, 20, 30]
    curr = head
    while curr:
        curr.key = key_list.pop()
        curr = curr.next
    return head


def PrintLinkedList(head):
    curr = head
    while curr:
        print(curr.key, end=" ")
        curr = curr.next


head = ReverseLinkedList(head)
PrintLinkedList(head)
