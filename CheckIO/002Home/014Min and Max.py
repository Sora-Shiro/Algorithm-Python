'''
In this mission you should write you own py3 implementation
(but you can use py2 for this) of the built-in functions min and max.
Some builtin functions are closed here: import, eval, exec, globals.
Don't forget you should implement two functions in your code.
max(iterable, *[, key]) or min(iterable, *[, key])
max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])
Return the largest (smallest) item in an iterable or the largest(smallest) of two or more arguments.
If one positional argument is provided, it should be an iterable.
The largest (smallest) item in the iterable is returned. If two or more positional arguments are provided,
the largest (smallest) of the positional arguments is returned.
The optional keyword-only key argument specifies a function of one argument that is used to
extract a comparison key from each list element (for example, key=str.lower).
If multiple items are maximal (minimal), the function returns the first one encountered.

-- Python Documentation (Built-in Functions)

Input: One positional argument as an iterable or two or more positional arguments.
Optional keyword argument as a function.
Output: The largest item for the "max" function and the smallest for the "min" function.
Precondition: All test cases are correct and functions don't have to raise exceptions.
'''

def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if key == None:
        key = lambda x : x
    result = args[0]
    if len(args)>1 and isinstance(args[0], list):
        result = args[0]
        min_ele = key(result)
        if isinstance(result, list):
            min_ele = result[0]
        for ll in args:
            if isinstance(key(ll), list):
                for ele in ll:
                    print min_ele
                    if min_ele > ele:
                        min_ele = ele
                        result = ll
                        print ll
            else:
                if min_ele > key(ll):
                    result = ll
                    min_ele = key(result)
        return result
    if isinstance(result, int) or isinstance(result, float):
        min_ele = key(result)
        for ele in args:
            if min_ele > key(ele):
                result = ele
                min_ele = key(result)
        return result
    args_new = result
    it = iter(args_new)
    result = it.next()
    min_ele = key(result)
    while 1:
        try:
            ele = it.next()
        except StopIteration:
            break
        if min_ele > key(ele):
            result = ele
            min_ele = key(result)
    return result

def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if key == None:
        key = lambda x : x
    result = args[0]
    if len(args)>1 and isinstance(args[0], list):
        result = args[0]
        min_ele = result
        if isinstance(result, list):
            min_ele = result[0]
        for ll in args:
            if isinstance(key(ll), list):
                for ele in ll:
                    print min_ele
                    if min_ele < ele:
                        min_ele = ele
                        result = ll
                        print ll
            else:
                if min_ele < key(ll):
                    result = ll
                    min_ele = key(result)
        return result
    if isinstance(result, int) or isinstance(result, float):
        min_ele = key(result)
        for ele in args:
            if min_ele < key(ele):
                result = ele
                min_ele = key(result)
        return result
    args_new = result
    it = iter(args_new)
    result = it.next()
    min_ele = key(result)
    while 1:
        try:
            ele = it.next()
        except StopIteration:
            break
        if min_ele < key(ele):
            result = ele
            min_ele = key(result)
    return result

'''
Clear:
1.
def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=reverse)[0]
​
​
def min(*args, key=None):
    return get_first_from_sorted(args, key, False)
​
​
def max(*args, key=None):
    return get_first_from_sorted(args, key, True)

Creative:
2.
min, max = (lambda *args, key=None, r=r: sorted(args[0] if len(args) == 1
    else args, key=key, reverse=r)[0] for r in range(2))
'''


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
