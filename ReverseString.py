def reverseNoExtraMemory(s):
    """ Reverses a String without using extra memory"""
    return "".join(reversed(s))


# Test

def testReverseNoExtraMemory():
    assert reverseNoExtraMemory("") == ""
    assert reverseNoExtraMemory("a") == "a"
    assert reverseNoExtraMemory("0") == "0"
    assert reverseNoExtraMemory("0ab") == "ba0"
    print("All tests passed")


if __name__ == '__main__':
    testReverseNoExtraMemory()
