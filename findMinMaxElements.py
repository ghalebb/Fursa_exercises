def find_min_max_elements(arr):
    """ This function return min and max elements in a given array. Assuming len(arr)>0"""
    min_val = float("inf")
    max_val = float("-inf")

    for num in arr:
        if num < min_val:
            min_val = num
        if max_val < num:
            max_val = num
    return min_val,max_val

#Test
def test_find_min_max_elements():
    assert find_min_max_elements([0,2,4,6,-7]) == (-7,6)
    assert find_min_max_elements([0,2,0,6,-7,-7,6]) == (-7,6)
    assert find_min_max_elements([4]) == (4,4)
    assert find_min_max_elements([0,100]) == (0,100)
    assert find_min_max_elements([-99,-100]) == (-100,-99)
    assert find_min_max_elements([9,400,3,234]) == (3,400)
    print("Passed all tests!")

if __name__ == '__main__':
    test_find_min_max_elements()