import string

text = str(input('input, the word or the text!'))
WORDLIST_FILENAME = 'words.txt'

def build_shift_dict(shift):

    lower = string.ascii_lowercase
    lower_shift = lower[shift:] + lower[:len(lower) + shift]
    capital = string.ascii_uppercase
    capital_shift = capital[shift:] + capital[:len(capital) + shift]

    lower_dict = {}
    for n in range(len(lower)):
        lower_dict[lower[n]] = lower_shift[n]
    capital_dict = {}
    for n in range(len(lower)):
        capital_dict[capital[n]] = capital_shift[n]
    dicti = {**lower_dict, **capital_dict}
    return dicti


def apply_shift(shift, text):



    c = build_shift_dict(shift)
    d_text = []
    for l in text:
        try:
            l = c[l]
            d_text.append(l)
        except:
            d_text.append(l)
    return ''.join(d_text)


def load_words(file_name):

    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


def is_word(word_list, word):

    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

#apply_shift(7, text)

d_text = 'P aopur aoha vby dvysk pz dvuklymbs wshjl av spcl!'

def decypher(text,word_list):
    dt = text.split()
    lmax = 0
    imax = 0

    for i in range(0,25):
        l = []
        for word in dt:
            t = apply_shift(i, word)
            if is_word(word_list, t):
                l.append(t)
            llen = len(l)
            if llen > lmax:
                lmax = llen
                imax = i


    best = apply_shift(imax, text)

    return imax, best



word_list = load_words(WORDLIST_FILENAME)

print(decypher(d_text,word_list))