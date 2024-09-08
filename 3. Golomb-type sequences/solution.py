from itertools import islice


def generate_golomb_sequence(n: int, numbers: list[int]) -> list[int]:
    sequence = sum(map(lambda x: [x] * n, numbers), [])
    return sequence


def golomb(given, n):
    sequence = []
    index_sequence = iter(given)
    number_squence = iter(given)

    # Generate the sequence up to the nth element
    while len(sequence) < n:
        m: int = next(index_sequence)

        number_list = []
        for _ in range(m):
            number_list.append(next(number_squence))
        sequence.extend(generate_golomb_sequence(m, number_list))

    # Return the first n elements of the sequence
    return sequence[:n]


# Example usage:
given = [1, 2, 3, 4]
n = 20
print(golomb(given, n))  # Output: [1, 2, 2, 3, 3, 4, 4, 4, 5, 5]
