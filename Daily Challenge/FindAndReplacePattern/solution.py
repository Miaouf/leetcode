class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def word_pattern(word):
            order = []
            n = -1
            ans = ""
            for letter in word:
                if(letter in order):
                    ans += str(order.index(letter))
                    
                else:
                    n += 1
                    order.append(letter)
                    ans += str(n)
            return ans
        
        match_pattern = word_pattern(pattern)
        ans = []
        
        for word in words :
            if(word_pattern(word) == match_pattern):
                ans.append(word)
                
        return ans
                    
