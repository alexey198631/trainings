def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise

    You should be thinking about 3 situations:
What happens when the string is empty?

What happens when the string is of length 1?

What happens when the test character equals the middle character?

Ищет, находится ли символ внутри строки

    '''
    # Your code here

    if aStr == '':
        return False
    elif len(aStr) == 1:
        testChar = aStr
    else:
        testChar = aStr[(len(aStr) // 2):(len(aStr) + 2) // 2]
    if char == testChar:
        return True
    elif char < testChar:
        return isIn(char, aStr[:((len(aStr) + 2) // 2)-1])
    elif char > testChar:
        return isIn(char, aStr[((len(aStr) // 2))+1:])
    else:
        return False


print(isIn('i', 'iz'))


"""
Решение от автора:

def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])


"""



"""
Определение палиндрома


def isPalindrome (s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))


print(isPalindrome('av'))




    def toChars(aStr):
        aStr = aStr.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
"""