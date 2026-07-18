
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)


def InsertInSortedLL(head, data):
    temp = Node(data)
    curr = head

    if head is None:
        return temp

    if temp.data < head.data:
        temp.next = head
        return temp

    while curr.next and curr.next.data < temp.data:
        curr = curr.next

    temp.next = curr.next
    curr.next = temp
    return head


def PrintLinkedList(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next


head = InsertInSortedLL(head, 25)
PrintLinkedList(head)
