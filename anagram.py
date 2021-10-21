from collections import Counter as C
def anagram(nums, n):
    word_list=[]
    anagrams=[]
   
    for i in nums:
        word_list.clear()
        #word_list.append(i)
        for j in range (1, n):
            
            if C(i)==C(nums[j]):
                word_list.append(nums[j])
        anagrams.append(len(word_list))
    return max(anagrams)         


print(anagram(["cats","caller","dogs","cellar","parrots","recall"], 6))  #3
