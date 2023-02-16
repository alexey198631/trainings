import string

def apply_shift(text, shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift

    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
         down the alphabet by the input shift
    '''
    lower = string.ascii_lowercase
    lower_shift = lower[shift:] + lower[:len(lower) + shift]
    print(lower_shift)
    capital = string.ascii_uppercase
    capital_shift = capital[shift:] + capital[:len(capital) + shift]
    print(capital_shift)

    print(lower)
    print(lower_shift)

    lower_dict = {}
    for n in range(len(lower)):
        lower_dict[lower[n]] = lower_shift[n]
    capital_dict = {}
    for n in range(len(lower)):
        capital_dict[capital[n]] = capital_shift[n]
    c = {**lower_dict, **capital_dict}
    print(c)
    d_text = []
    for l in text:
        try:
            l = c[l]
            d_text.append(l)
        except:
            d_text.append(l)
    return ''.join(d_text)

print(apply_shift('we are taking 6.00.1x', 3))