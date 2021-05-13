class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def transform(x):
            L = [x]
            for i in range(1,len(x)):
                L.append("{}.{}".format(x[:i],x[i:]))
            return L
        
        def isValid(x):
            if("." in x):
                return not(x[0] == "0" and x[1:2] != ".") and not(x[-1] == "0")
            else:
                return not (x[0] == "0" and x[1:2] != "")
                
        ans = []
        n = len(s)-2
        for i in range(1,n):
            a, b = s[1:i+1], s[i+1:n+1]
            for s1 in transform(a):
                for s2 in transform(b):
                    if(isValid(s1) and isValid(s2)):
                        ans.append("({}, {})".format(s1,s2))
                        
        return ans
