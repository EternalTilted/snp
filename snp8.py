def multiply_numbers(inputs=''):
    res = None
    inputs = list(str(inputs))

    for i in inputs:
        if i.isdigit():
            if res == None:
                res = int(i)
            else:
                res *= int(i)

    return res

print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))

