x = 'qcqbrvhbh'
p = 0
length = 0

for i in range(len(x)-2):
    p = x[i]
    print(x[i],x[i+1])

    while x[i] <= x[i+1]:
        p += x[i+1]
        i += 1
    if len(p) > length:
        length = len(p)
        longest = p


print('Longest substring in alphabetical order is: ' + str(longest))
