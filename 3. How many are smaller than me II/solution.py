from bisect import bisect_left


def smaller(arr):
    popped_items = []
    result = []
    arr.reverse()
    for index, value in enumerate(arr):
        insert_index = bisect_left(popped_items, value)
        result.append(insert_index)
        # The insert is O(n) operation, so the total time complexity is O(n^2)
        popped_items.insert(insert_index, value)
    return list(reversed(result))
