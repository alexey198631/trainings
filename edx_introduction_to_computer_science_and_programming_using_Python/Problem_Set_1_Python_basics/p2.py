# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print

s = 'azcbobobegghakl'
x = 'bob'
count = 0


for n in range(0,len(s)):
    if len(s[n:(n+len(x))])== len(x):
        if s[n:(n + len(x))] == x:
            count += 1
    else: break
print(f"Number of times {x} occurs is:",count)
