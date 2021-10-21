def anagram(n, word_list):
    ascii_of_word_list = []
    
    for i in word_list:
        ascii_of_word = 0
        for j in i:
            ascii_of_word += ord(j)
        ascii_of_word_list.append(ascii_of_word)

    count_dict = dict(zip(set(ascii_of_word_list), [0] * n))

    for i in ascii_of_word_list:
        count_dict[i] += 1

    return max(count_dict.values())

print(anagram(6, ["cats", "caller", "dogs", "cellar", "parrots", "recall"]))
        
