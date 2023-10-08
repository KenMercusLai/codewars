def smaller(arr):
    popped_items = []
    result = []
    index = len(arr) - 1
    while index >= 0:
        popped_items = sorted(arr[index:])
        result.insert(0, popped_items.index(arr[index]))
        index -= 1
    return result
