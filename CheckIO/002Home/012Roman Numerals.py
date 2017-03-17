'''
Roman numerals come from the ancient Roman numbering system.
They are based on specific letters of the alphabet which are combined to signify the sum
(or, in some cases, the difference) of their values. The first ten Roman numerals are:
I, II, III, IV, V, VI, VII, VIII, IX, and X.
The Roman numeral system is decimal based but not directly positional and does not include a zero.
Roman numerals are based on combinations of these seven symbols:
Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)
More additional information about roman numerals can be found on the Wikipedia article.
For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
Input: A number as an integer.
Output: The Roman numeral as a string.
Precondition: 0 < number < 4000
'''

def checkio(data):
    romanNum = [1, 5, 10, 50, 100, 500, 1000]
    romanC = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    result = ""
    i = 6
    decrease = romanNum[6]
    while 1:
        if data == 0:
            break
        quot = data//decrease
        if quot == 0:
            i -= 1
            decrease = romanNum[i]
            continue
        result += romanC[i]*(quot)
        data -= decrease*quot
    i = 0
    while i < 5:
        if romanC[i]*4 in result:
            result = result.replace(romanC[i]*4, romanC[i] + romanC[i+1])
            attention = romanC[i+1] + romanC[i] + romanC[i+1]
            relax = romanC[i] + romanC[i+2]
            if attention in result:
                result = result.replace(attention, relax)
        i += 2
    return result

'''
Clear:
1.
def checkio(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result
2.
def checkio(data):
    ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thous = ["","M","MM","MMM","MMMM"]

    t = thous[data // 1000]
    h = hunds[data // 100 % 10]
    te = tens[data // 10 % 10]
    o =  ones[data % 10]

    return t+h+te+o
3.
DIGITS = [
        ('M', 1000, 900),
        ('D', 500, 400),
        ('C', 100, 90),
        ('L', 50, 40),
        ('X', 10, 9),
        ('V', 5, 4),
        ('I', 1, 1),
    ]
TO_DIGIT = {value: character for character, value, _ in DIGITS}
def checkio(number):
    result = ''
    # Work from largest to smallest
    for digit, value, limit in DIGITS:
        while number >= limit:
            # Handle the special case of subtracting smaller numerals.
            if number < value:
                delta = value - limit
                result += TO_DIGIT[delta]
                number += delta
            result += digit
            number -= value
    return result

Creative:
4.
import formatter, functools
checkio = functools.partial(formatter.AbstractFormatter.format_roman, None, 'I')
'''



    # romanList = {1 : 'I', 5 : 'V', 10 : 'X' , 50 : 'L' , 100 : 'C', 500 : 'D', 1000 : 'M'}
    # romanList = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    # num = 0
    # for c in data:
    #     num += romanList[c]
    # return num

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
