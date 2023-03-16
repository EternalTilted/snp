def connect_dicts(dict1, dict2):
    res = dict()

    if sumvalue(dict1) > sumvalue(dict2):
        res = dict2
        for i in dict1:
            res[i] = dict1[i]
    else:
        res = dict1
        for i in dict2:
            res[i] = dict2[i]

    
    for i in list(res.keys()):
        if res[i] < 10:
            res.pop(i)

    
    return dict(sorted(res.items(), key=lambda item: item[1]))

def sumvalue(dict):
    sum = 0
    for i in dict:
        sum+=dict[i]

    return sum

print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }))
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))

