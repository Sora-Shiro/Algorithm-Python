'''
"Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.
You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.
Input: A number as an integer.
Output: The answer as a string.
Precondition: 0 < number ≤ 1000
'''

#Your optional code here
#You can import some modules or create additional functions


def checkio(number):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    flag3 = 0
    flag5 = 0
    if number%3 == 0:
        flag3 = 1
    if number%5 == 0:
        flag5 = 1
    if flag3 and flag5:
        return str("Fizz Buzz")
    if flag3:
        return str("Fizz")
    if flag5:
        return str("Buzz")
    return str(number)
    '''
    Clear:
    1.
    if number % 15 == 0:
        return 'Fizz Buzz'
    if number % 5 == 0:
        return 'Buzz'
    if number % 3 == 0:
        return 'Fizz'
    return str(number)

    Creative:
    2.
    checkio=lambda n:" ".join("BuFi#"[-k:2-k]+"zz"for k in(3,5)if n%k==0)or str(n)
    3.
    checkio=lambda n:("Fizz "*(1-n%3)+"Buzz "*(1-n%5))[:-1]or str(n)
    #str times negative is ""
    '''

#Some hints:
#Convert a number in the string with str(n)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
