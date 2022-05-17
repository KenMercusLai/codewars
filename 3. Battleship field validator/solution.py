# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)


def frequencies(s):
    return [(i, s.count(i)) for i in set(s)]


def construct_tree(s):
    converted_s = list(map(lambda x: {'code': "", 'letter': x[0], 'count': x[1], 'children': []}, s))
    converted_s = sorted(converted_s, key=lambda x: x['count'], reverse=True)
    while len(converted_s) > 1:
        last_0 = converted_s.pop()
        last_0['code'] = '1'
        last_1 = converted_s.pop()
        last_1['code'] = '0'
        new_node = {'code': "", 'letter': None, 'count': last_0['count'] + last_1['count'],
                    'children': [last_0, last_1]}
        converted_s += [new_node]
        converted_s = sorted(converted_s, key=lambda x: x['count'], reverse=True)
    return converted_s


def simplify_tree(constructed_tree, initial_code, translated):
    for i in constructed_tree:
        if i['children']:
            translated.update(simplify_tree(i['children'], initial_code + i['code'], translated))
        else:
            translated[i['letter']] = initial_code + i['code']
    return translated


# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def translate(freqs):
    encoded_tree = construct_tree(freqs)
    return simplify_tree(encoded_tree, '', {})


def encode(freqs, s):
    if len(freqs) < 2:
        return None
    translated_code = translate(freqs)
    return ''.join([translated_code[i] for i in s])


def invert_code(translated_code):
    return {v: i for i, v in translated_code.items()}


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    if len(freqs) < 2:
        return None

    translated_code = translate(freqs)
    inverted_code = invert_code(translated_code)
    ret = ''
    bit = ''
    while bits:
        bit += bits[0]
        bits = bits[1:]
        if bit in inverted_code:
            ret += inverted_code[bit]
            bit = ''
    return ret


if __name__ == '__main__':
    fs = frequencies("aaaabcc")
    assert encode(fs, "aaaabcc") is not None
    assert len(encode(fs, "aaaabcc")) == 10
    assert encode(fs, []) == ''
    assert decode(fs, []) == ''
    assert decode(fs, encode(fs, "aaaabcc")) == "aaaabcc"
