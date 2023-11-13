class Node:
    def __init__(self, val=0, nex=None):
        self.val = val
        self.next = nex


def findMiddle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def testFindMiddle():
    # case1
    firstList = Node(0, Node(1, Node(2, Node(3, Node(4)))))
    assert findMiddle(firstList).val == 2

    print("Test 1 passed")


if __name__ == '__main__':
    testFindMiddle()