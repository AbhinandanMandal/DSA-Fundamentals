
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


def SortedInserted(head, x):
    temp = Node(x)

    if head == None:
        return temp

    elif x < head.key:
        temp.next = head
        return temp

    else:
        curr = head
        while curr.next != None and curr.next.key < x:
            curr = curr.next
        temp.next = curr.next
        curr.next = temp
        return head


def PrintLinkedList(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = SortedInserted(head, 25)
PrintLinkedList(head)
