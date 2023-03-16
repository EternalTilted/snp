def combine_anagrams(words_array):
    res = []

    while words_array != []:
        if words_array[0] != []:
            buf_mas = [words_array.pop(0)]
            buf = set(buf_mas[0])

            for i in range(len(words_array)):

                if buf == set(words_array[i]):
                    buf_mas += [words_array.pop(i)]
                    words_array.append([])

            res.append(buf_mas)
            
        else:
            words_array.pop(0)
        
        
        
    return res

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))



