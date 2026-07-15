
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


def IsLinkedListSorted(head):
    if head is None and head.next is None:
        return True

    # Condition for if the linked list is like of
    # 3,4,5,5,5,5,5,6
    curr = head
    while curr.next and curr.key == curr.next.key:
        curr = curr.next
    if curr.next is None:
        return True

    # At initial we're considering linkedlist as
    # 1,2,3,4,5, None
    ascending = curr.key < curr.next.key
    while curr.next:
        if ascending:
            if curr.key > curr.next.key:
                return False
        else:
            if curr.key < curr.next.key:
                return False
        curr = curr.next
    return True


print(IsLinkedListSorted(head))
