"""
Write a program that prompts for a file name, then opens that file and reads through the file,
and print the contents of the file in upper case.
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
Use words.txt as the file name
"""

# file words.txt is in 'data_files' forlder

file_name = 'data_files/' + input("Enter file name: ")
file = open(file_name)
text = file.read()
upper_text = text.upper().strip()
print('\n', upper_text)