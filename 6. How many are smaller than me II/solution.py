def smaller(arr):
    popped_items = []
    result = []
    while arr:
        item = arr.pop()
        popped_items.append(item)
        popped_items = sorted(popped_items)
        result.insert(0, popped_items.index(item))
    return result
