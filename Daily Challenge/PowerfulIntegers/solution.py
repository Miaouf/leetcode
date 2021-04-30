class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        i = 1
        j = 1
        
        dic = []
        L = []
        
        def rec(x,y,i,j,bound):
            if(i+j <= bound):
                L.append(i+j)

                if([i*x,j] not in dic):
                    dic.append([i*x,j])
                    rec(x,y,i*x,j,bound)

                if([i,j*y] not in dic):
                    dic.append([i,j*y])
                    rec(x,y,i,j*y,bound)  
                        
        rec(x,y,1,1,bound)

        return set(L)
