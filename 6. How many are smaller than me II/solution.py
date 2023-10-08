from bisect import bisect_left


def smaller(arr):
    popped_items = []
    result = []
    index = len(arr) - 1
    while index >= 0:
        insert_index = bisect_left(popped_items, arr[index])
        result.append(insert_index)
        popped_items.insert(insert_index, arr[index])
        index -= 1
    return list(reversed(result))
