
al = "abcdefghjiklmnoprstuqvwxyz"
x = "qcqbrvhbh"

i = 0
l = 0
p = 0
y = 0

for z in range(len(x)):
    while i < len(x) and x[z:i+1] in al:
        if l < len(x[z:i+1]):
            l = len(x[z:i+1])
            p = z
            y = i + 1

        i += 1

print(l, x[p:y])


#как бы я сделал все отлиично, только задание было другим.