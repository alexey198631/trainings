def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
   print(set1,set2)
   if len(set1) == 0:
      return set2
   elif set1[0] in set2:
      return union(set1[1:], set2)
   else:
      return set1[0] + union(set1[1:], set2)


#print(sorted(union('abcdefgj','ab')))

#list = 'abc'
#print(list[0])

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    print(x,a)
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)

print(rem(7,5))

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)

print(f(3))