def min_max_subarrray(array):
    sub_lists = []
    array_max = sorted(array)[-1]
    array_min = sorted(array)[0]
    for i in range(len(array) + 1):
        for j in range(i):
            sub_lists.append(array[j: i])
    return min([x for x in sub_lists if (array_max in x) and (array_min in x)],key=len)
