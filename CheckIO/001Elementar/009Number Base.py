'''
Do you remember the radix and Numeral systems from math class? Let's practice with it.
You are given a positive number as a string along with the radix for it.
Your function should convert it into decimal form. The radix is less than 37 and greater than 1.
The task uses digits and the letters A-Z for the strings.
Watch out for cases when the number cannot be converted. For example: "1A" cannot be converted with radix 9.
For these cases your function should return -1.
Input: Two arguments. A number as string and a radix as an integer.
Output: The converted number as an integer.
Precondition:
re.match("\A[A-Z0-9]\Z", str_number)
0 < len(str_number) ≤ 10
2 ≤ radix ≤ 36
'''

def checkio(str_number, radix):
    length = len(str_number)
    i = 1
    num = 0
    for c in str_number:
        if(c.isalpha()):
            if(ord(c)-54 > radix):
                return -1
            num += (ord(c)-55) * (radix ** (length-i))
        else:
            if(int(c) >= radix):
                return -1
            num += int(c) * (radix ** (length-i))
        i += 1
    return num

'''
Clear:
1.
def checkio(*a):
    try: return int(*a)
    except ValueError: return -1
2.
def checkio(str_number, radix):
   try: return int(str_number, radix)
   except : return -1

Creative:
3.
checkio=lambda s,r:(r>int(max(s),36))-1or int(s,r)
4.
def checkio(*args):
    exec "try: res = int(%r, %s)\nexcept: res = -1" % args
    return res
5.
def checkio(str_number, radix):
    glyphs = [x for x in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    power = 0
    result = 0
    for digit in reversed(str_number):
        value = glyphs.index(digit)
        if value >= radix:
            return -1
        result += value * radix ** power
        power += 1
    return result

'''



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
