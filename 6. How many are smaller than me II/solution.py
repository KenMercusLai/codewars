from bisect import insort


def smaller(arr):
    popped_items = []
    result = []
    index = len(arr) - 1
    while index >= 0:
        insort(popped_items, arr[index])
        result.append(popped_items.index(arr[index]))
        index -= 1
    return list(reversed(result))
