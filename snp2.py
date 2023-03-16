
def coincidence(list = [], range=()):
    buf = []
    
    for i in list:
        if (type(i) == int or type(i) == float or type(i) == complex) and (i>=range[0] and i<=range[-1]):
            buf.append(i)

    return buf

print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))


