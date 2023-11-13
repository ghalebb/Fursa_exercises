class Node:
    def __init__(self, val=0, nex=None):
        self.val = val
        self.next = nex


def findCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def testFindCycle():
    e = Node("e")
    d = Node("d", e)
    c = Node("c", d)
    b = Node("b", c)
    a = Node("a", b)
    e.next = c

    assert findCycle(a) == True
    print("Test 1 passed")

    e.next = None

    assert findCycle(a) == False

    print("Test 2 passed")
    f = Node("a")
    f.next = f
    assert findCycle(f) == True
    print("Test 3 passed")


if __name__ == '__main__':
    testFindCycle()