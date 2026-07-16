
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)


def SumTheNodes(head):
    curr = head
    node_sum = 0
    while curr:
        node_sum += curr.key
        curr = curr.next
    return node_sum


print(SumTheNodes(head))
