def next_smaller(n):
    # no need to check if the number is single-digit
    if n < 10:
        return -1

    n = list(str(n))
    # no need to check if the digits are already in the smallest combination
    if sorted(n) == n:
        return -1

    # Starting from the second last digit A, find the max digit that is smaller than A
    # swap these two digits and sort the digits after A descend
    for i in range(len(n) - 2, -1, -1):
        smaller_numbers_on_right = list(filter(lambda x: x < n[i], n[i + 1 :]))
        if not smaller_numbers_on_right:
            continue
        biggest = max(smaller_numbers_on_right)
        n[i], n[n[i + 1 :].index(biggest) + i + 1] = (
            n[n[i + 1 :].index(biggest) + i + 1],
            n[i],
        )
        n[i + 1 :] = sorted(n[i + 1 :], reverse=True)
        if n[0] == "0":
            return -1
        return int("".join(n))
    return -1
