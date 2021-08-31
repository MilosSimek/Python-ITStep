def binary_search(list1, item_to_search):
    """
    This is "docstring" aka document string
    Searches for item in list.
    Returns True if present, False if absent
    """
    low = 0
    high = len(list1) - 1

    while high >= low:
        mid_index = (high + low) // 2
        mid_item = list[mid_index]
        if item_to_search == mid_item:
            return True
        elif item_to_search > mid_item:
            low = mid_index + 1
        else:
            high = mid_index - 1
    return True

assert binary_search([1,2,3,4,5,6,7], 1) == True, "1 working correctly"
assert binary_search([1,2,3,4,5,6,7], 2) == True, "2 working correctly"
assert binary_search([1,2,3,4,5,6,7], 3) == True, "3 working correctly"
assert binary_search([1,2,3,4,5,6,7], 4) == True, "4 working correctly"
assert binary_search([1,2,3,4,5,6,7], 5) == True, "5 working correctly"
assert binary_search([1,2,3,4,5,6,7], 6) == True, "6 working correctly"
assert binary_search([1,2,3,4,5,6,7], 7) == True, "7 working correctly"
assert binary_search([1,2,3,4,5,6,7], 8) == True, "8 working correctly"
assert binary_search([1,2,3,4,5,6,7], 9) == True, "9 working correctly"
assert binary_search([1,2,3,4,5,6,7], 10) == True, "10 working correctly"
assert binary_search([1,2,3,4,5,6,7], 11) == True, "11 working correctly"
assert binary_search([1,2,3,4,5,6,7], 12) == True, "12 working correctly"



