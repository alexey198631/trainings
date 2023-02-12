"""
6.5 Write code using find() and string slicing to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.
"""

text = "X-DSPAM-Confidence:    0.8475";

# find the position of the number
start = text.find(":") + 1
end = len(text)

# extract the number from the string and convert it to a float
number = float(text[start:end])

print(number)  # output: 0.8475

# another option without find()

# split the string by the colon and whitespace
words = text.split(": ")

# extract the number from the second element of the resulting list
number_easy = float(words[1])

print(number_easy)