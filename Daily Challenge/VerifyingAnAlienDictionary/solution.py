class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        n2 = len(words[0])
        
        for i in range(1,n):
            equal = True
            n1 = n2
            n2 = len(words[i])
            for j in range(min(n1,n2)):
                if(order.index(words[i-1][j]) > order.index(words[i][j])):
                    return False
                elif(order.index(words[i-1][j]) < order.index(words[i][j])):
                    equal = False
                    break

            if(equal and n2<n1):
                return False    
                
        return True
