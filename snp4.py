def sort_list(list):

    if list == []:
        return []

    minel = min(list)
    maxel = max(list)

    for i in range(len(list)):
        if list[i] == minel:
            list[i] = maxel
        elif list[i] == maxel:
            list[i] = minel
    
    return list + [minel]


print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))