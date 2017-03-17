'''
You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...) then
multiply this summed number and the final element of the array together.
Don't forget that the first element has an index of 0.
For an empty array, the result will always be 0 (zero).
Input: A list of integers.
Output: The number as an integer.
Precondition: 0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
'''

def checkio(array):
    length = len(array)
    if length == 0:
        return 0
    count = result = 0
    while count < length:
        result += array[count]
        count += 2
    result *= array[length-1]
    return result
'''
Clear:
1.
if len(array) == 0: return 0
return sum(array[0::2]) * array[-1]
2.
checkio=lambda x: sum(x[::2])*x[-1] if x else 0
3.
return sum(el for el in array[::2]) * array[-1] if array else 0
4.
if not array:   return 0
return sum(array[::2])*array[-1]

Creative:
5.
checkio = lambda array: sum(array[::2]) * sum(array[-1:])
'''

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
