import string

lower = string.ascii_lowercase
capital = string.ascii_uppercase
p = string.punctuation
d = string.digits

shift = 3

lower_shift = lower[-shift:] + lower[:len(lower) - shift]
capital_shift = capital[-shift:] + capital[:len(capital) - shift]


def shift(text, text_shift):
    str_dict = {}
    for n in range(len(text)):
        str_dict[text[n]] = text_shift[n]
    return str_dict


new = shift(lower, lower_shift) | (shift(capital, capital_shift))
print(new)

a = shift(lower, lower_shift)
b = shift(capital, capital_shift)

c = {**a, **b}
print('c', c)

text = 'I love you, baby'
text_list = []
for l in text:
    text_list.append(l)

print(text_list)

d_text = []

for l in text_list:
    try:
        l = c[l]
        d_text.append(l)
    except:
        d_text.append(l)

print(''.join(d_text))

"""
for l in str:
    str_l_list.append(l)

print(str_list)

print(str_dict)

for n in range(len(str_list)):

    try:
        str_dict[str_list[n]] = str_list[n+3]
    except:
        str_dict[str_list[n]] = 0

print(str_dict)

"""
