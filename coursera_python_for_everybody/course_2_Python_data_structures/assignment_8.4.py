"""
8.4 Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words.
For each word on each line check to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""

# file romeo.txt is in 'data_files' forlder

file_name = 'data_files/' + input("# Use the file name 'romeo.txt' as the file name\nEnter file name: ")

# Open the file and read it line by line
with open(file_name) as file:
    words_list = []
    for line in file:
        # Split the line into a list of words
        words = line.split()

        # Check if each word is already in the list and if not, append it
        for word in words:
            if word not in words_list:
                words_list.append(word)

# Sort and print the resulting words in alphabetical order
words_list.sort()
print(words_list)