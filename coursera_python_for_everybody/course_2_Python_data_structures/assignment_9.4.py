"""
9.4 Write a program to read through the mbox-short.txt
and figure out who has the sent the greatest number of mail messages.
The program looks for 'From ' lines
and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the
sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary
using a maximum loop to find the most prolific committer.
"""

# file mbox-short.txt is in 'data_files' forlder

file_name = 'data_files/' + input("# Use the file name mbox-short.txt as the file name\nEnter file name: ")

# Open the file and read it line by line
with open(file_name) as file:
    count = 0
    temp = []
    email_count = {}
    for line in file:
        if line.startswith('From '):
            words = line.split()
            if len(words) > 1:
                if words[1] not in temp:
                    email_count[words[1]] = email_count.get(words[1], 0) + 1
    max_value = max(email_count.values())
    inverted_dict = {v: k for k, v in email_count.items()}
    # Access the key by its value
    key_commiter = inverted_dict.get(max_value)

print(f'The most prolific committer {key_commiter} with {max_value} emails')