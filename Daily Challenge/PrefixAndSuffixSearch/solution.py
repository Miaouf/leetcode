class WordFilter:

    def __init__(self, words: List[str]):
        self._dic = {}
        
        for k in range(len(words)):
            n = len(words[k])
            for i in range(min(10,n)):
                for j in range(min(10,n)):
                    self._dic[(words[k][:1+i],words[k][j:])] = k
        

    def f(self, prefix: str, suffix: str) -> int:
        return self._dic[(prefix,suffix)]
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
