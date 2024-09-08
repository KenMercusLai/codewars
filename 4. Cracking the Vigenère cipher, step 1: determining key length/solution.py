# Kasiski examination https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Kasiski_examination
from functools import reduce
from collections import Counter


def find_repeated_substrings(text: str, min_length=3, max_length=100):
    substrings = {}
    positions = {}
    for i in range(len(text) - min_length + 1):
        for j in range(i + min_length, i + min_length + max_length):
            substr = text[i:j]
            if max_length >= len(substr) >= min_length:
                substrings[substr] = substrings.get(substr, 0) + 1
                if substr not in positions:
                    positions[substr] = []
                positions[substr].append(i)

    return {
        s: (count, list(set(positions[s])))
        for s, count in substrings.items()
        if count > 1
    }


def factors(n: int) -> set[int]:
    return set(
        reduce(
            list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)
        )
    )


def find_all_factors(repeated):
    all_factors = {}
    for substr, (count, pos) in repeated.items():
        pos_pairs = zip(pos, pos[1:])
        diff_poses = list(map(lambda x: abs(x[1] - x[0]), pos_pairs))
        for i in diff_poses:
            if i not in all_factors:
                all_factors[i] = factors(i)
    return all_factors


def count_factors(all_factors):
    # Flatten the sets and count occurrences
    all_numbers = [
        num for value_set in all_factors.values() for num in value_set if num > 2
    ]
    number_counts = Counter(all_numbers)

    # Sort the results by count (descending) and then by number (ascending)
    sorted_counts = sorted(number_counts.items(), key=lambda x: (-x[1], x[0]))
    max_count = max(item[1] for item in sorted_counts)
    most_frequent = sorted(
        [item[0] for item in sorted_counts if item[1] == max_count], reverse=True
    )
    return most_frequent


def get_key_length(cipher_text, max_key_length):
    repeated = find_repeated_substrings(cipher_text, 3, max_key_length)
    most_fre_factors = find_all_factors(repeated)
    return count_factors(most_fre_factors)[0]
