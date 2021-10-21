def anagram(n, word_list):
    ascii_of_word_list = []
    
    for i in word_list:
        ascii_of_word = 0
        for j in i:
            ascii_of_word += ord(j) - 97  # converts each char to it's ascii equivalent {-97}
                                          # and add all chars in the word together
        ascii_of_word_list.append(ascii_of_word)

    count_dict = dict(zip(set(ascii_of_word_list), [0] * n))    
    # makes a dict with items in ascii_of_word_list as keys and values being zero(0)
    for i in ascii_of_word_list:
        count_dict[i] += 1

    return max(count_dict.values())

print(anagram(6, ["cats", "caller", "dogs", "cellar", "parrots", "recall"]))

## found a case where the program will fail:
    ## say "ace" and "bbe"
    ## 0 + 2 + 4 == 1 + 1 + 4 
        
