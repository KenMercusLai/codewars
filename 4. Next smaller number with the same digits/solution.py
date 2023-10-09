def next_smaller(n):
    # no need to check if the number is single-digit
    if n < 10:
        return -1

    n = list(str(n))
    if sorted(n) == n:
        return -1

    # starting from the second last digit, find the first digit that is smaller than the digit on its right
    for i in range(len(n) - 2, -1, -1):
        if n[i] > n[i + 1]:
            for j in range(i + 1, len(n)):
                if n[j] < n[i]:
                    n[i], n[j] = n[j], n[i]
                    n[i + 1 :] = sorted(n[i + 1 :], reverse=True)
                    return int("".join(n))
    return -1
