"""
Implement a function that meets the specifications below.

def cipher(map_from, map_to, code):
   map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping.

For example,

cipher("abcd", "dcba", "dab") returns (order of entries in dictionary may not be the same)
({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
"""


def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. """

    key_code = {}
    # each key is a letter in map_from at index i and the corresponding value is the letter in map_to at index i
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]

    # decoded is a string that contains the decoded version of code using the key_code mapping
    decoded_d = {}
    lst = []
    for l in code:
        decoded_d[l] = key_code[l]
        lst.append(decoded_d[l])
    decoded = ''.join(lst)

    # returns a tuple of (key_code, decoded)
    return key_code, decoded


print(cipher("ac", "dk", "cac")) # output ({'a': 'd', 'c': 'k'}, 'kdk')
print(cipher("abcd", "dcba", "dab")) # output ({'a': 'd', 'b': 'c', 'c': 'b', 'd': 'a'}, 'adc')




