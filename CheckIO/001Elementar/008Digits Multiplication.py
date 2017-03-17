'''
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.
For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
Input: A positive integer.
Output: The product of the digits as an integer.
Precondition: 0 < number < 10^6
'''

def checkio(number):
    result = 1
    while number > 1:
        a = number % 10
        if(a != 0):
            result *= a
        number //= 10
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1

'''
Clear:
1.
def checkio(number):
    """
    Convert into the string and iterate.
    """
    res = 1
    for d in str(number):
        if(int(d)):
            res *= int(d)
    return res

2.
from functools import reduce
from operator import mul
​
def checkio(number):
    return reduce(mul, (int(x) for x in str(number) if x != '0'))

3.
def checkio(number):
    total = 1
    for i in str(number).replace('0', '1'):
        total *= int(i)
    return total

4.
def checkio(number):
    result = 1
    for digit in str(number).replace('0', ''):
        result *= int(digit)
    return result

Creative:
5.
checkio = lambda n: eval("*".join(i for i in str(n) if i != '0'))

6.
checkio=lambda n:(n%10 or 1)*checkio(n//10)if n else 1

'''
