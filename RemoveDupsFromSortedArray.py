def removeDuplicates(arr):
    k = 1
    for i in range(1, len(arr)):
        if arr[k - 1] != arr[i]:
            arr[k] = arr[i]
            k = k + 1
    return arr[:k]


def testRemoveDuplicates():
    # case1
    arr = removeDuplicates([0,0,1,2,3,3])
    assert arr == [0,1,2,3]
    print("Test 1 passed")

    #case 2
    arr = removeDuplicates([1,1,1,1,1])
    assert arr == [1]
    print("Test 2 passed")

    # case 3
    arr = removeDuplicates([-100,-100,0, 1, 1, 1, 100])
    assert arr == [-100,0,1,100]
    print("Test 3 passed")

if __name__ == '__main__':
    testRemoveDuplicates()