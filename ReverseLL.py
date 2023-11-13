class Node:
    def __init__(self, val=0, nex=None):
        self.val = val
        self.next = nex


def reverseLinkedList(head):
    prev = None
    curr = head
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev


def test_reverseLinkedList():
    firstList = Node(0, Node(1, Node(2, Node(3, Node(4)))))

    node = reverseLinkedList(firstList)
    for i in range(4, -1, -1):
        assert node.val == i
        node = node.next
    print("Test 1 passed!")


if __name__ == '__main__':
    test_reverseLinkedList()
