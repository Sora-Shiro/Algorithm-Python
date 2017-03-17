'''
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space).
The words contains only letters. You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.
Input: A string with words.
Output: The answer as a boolean.
Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
0 < len(words) < 100
'''

def checkio(words):
    count = 0
    to = 0
    while 1:
        if words[count] == ' ':
            if words[count-1].isalpha():
                to += 1
            if words[count-1].isdigit():
                to = 0
            if to == 3:
                return True
        count += 1
        if(count == len(words)):
            if to == 2 and words[count-1].isalpha():
                return True
            break
    return False
    # count = 0
    # toResult = 0
    # while 1:
    #     if count == len(words):
    #         print(words[count-1].isalpha())
    #         if words[count-1].isalpha() and toResult == 2:
    #             return True
    #         break
    #     if words[count].isalpha():
    #         count += 1
    #         continue
    #     if words[count].isdigit():
    #         count += 1
    #         toResult = 0
    #         continue
    #     if(words[count-1].isalpha()):
    #         toResult += 1
    #     print(toResult)
    #     if toResult == 3:
    #         return True
    #     count += 1
    # return False

    '''
    Clear:
    1.
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False

    Creative:
    1.
    checkio=lambda x:"www" in "".join('w' if w.isalpha() else 'd' for w in x.split())
    2.
    checkio=lambda x:"www" in "".join('dw'[w.isalpha()] for w in x.split())
    '''



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
