class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []  
        word = ""
        for i in range(len(s)):
            if(s[i] in word):
                res.append(word)
                while(s[i] in word):
                    word = word[word.index(s[i])+1:]
            word += s[i]
        res.append(word)
        return max(len(x) for x in res)
