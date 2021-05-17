class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x : len(x))
        dic = defaultdict(int)
        for word in words:
            n = len(word)
            if(n == 1):
                dic[word] = 1
            
            else:  
                max_v = 1
                for i in range(n):
                    n_word = word[:i]+word[i+1:]
                    if(n_word in dic):
                        max_v = max(max_v, dic[n_word]+1)
                dic[word] = max_v
        return max(dic.values())
