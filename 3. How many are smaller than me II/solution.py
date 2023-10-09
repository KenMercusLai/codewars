from bisect import bisect_left


def smaller(arr):
    popped_items = []
    result = []
    i = len(arr) - 1
    while i >= 0:
        insert_index = bisect_left(popped_items, arr[i])
        result.append(insert_index)
        popped_items.insert(insert_index, arr[i])
        i -= 1
    return list(reversed(result))
