"""
The code transforms str input from Roman Number to Integer Number
"""

def romanToInt(s: str) -> int:
    # create disctionary of values
    symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values = [1, 5, 10, 50, 100, 500, 1000]
    dt = {}
    for i, k in enumerate(symbols):
        dt[k] = values[i]
    # transform input in a list
    intput = list(s)
    # create result variable
    result = 0
    # cycle with exchange logic
    for i in range(len(s)):
        if i == (len(s) - 1):
            result = result + dt[s[i]]
        else:
            if dt[s[i]] < dt[s[i + 1]]:
                result = result - dt[s[i]]
            else:
                result = result + dt[s[i]]
    return result


print(romanToInt('III'), romanToInt('XLIII'), romanToInt('MCMXCIV'))

