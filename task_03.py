import math

def max_odd(list):
    res = None
    for i in list:
        if (type(i)==int or type(i)==float or type(i)==complex) and math.isclose(i%2, 1) and (res==None or res<i):
            res = i

    return res


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]) )

