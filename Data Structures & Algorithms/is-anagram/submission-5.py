class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #s = "xx"
        #t = "x"
        word_dict = {}
        for i in s:
            if i in word_dict:
                #print(i + " is in word_dict")
                #print(word_dict[i])
                word_dict[i] += 1
            else:
                #print(i + " is NOT in word_dict")
                word_dict[i] = 1
        #print(word_dict)
        for i in t:
            if (i in word_dict) and (word_dict[i] != 0):
                word_dict[i] -= 1
                if word_dict[i] == 0:
                    del word_dict[i]
            else:
                return False
        if word_dict:
            return False
        return True
        