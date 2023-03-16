def count_words(string):

    string = string.lower()
    string = ''.join([string[i] for i in range(len(string)) if (string[i].isalnum() or  string[i] == ' ')])
    string = string.split(' ')

    dict1 = dict()
    
    for i in string:
        if dict1.get(i) != None:
            dict1[i] =  dict1[i]+1
        elif i!='':
            dict1[i] = 1

    return dict1

print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
