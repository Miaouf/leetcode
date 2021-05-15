class Solution:
    def isNumber(self, s: str) -> bool:
        expo_possible = False
        has_int = False
        has_dot = False
        n = len(s)
        
        for i in range(n):
            if(s[i]=="."): #Dot
                if(has_dot == False and expo_possible == False):
                    has_dot = True
                    continue
                else:
                    return False

            if(s[i] == "+" or s[i] == "-"): #Sign
                if(i == 0 or (expo_possible == True and (s[i-1] == "e" or s[i-1] == "E"))):
                    continue
                else:
                    return False
            
            if(has_int == True and (s[i] == "e" or s[i] == "E")): #Exponential
                if(expo_possible == False):
                    has_int = False
                    expo_possible = True
                    continue
                else: 
                    return False
            
            if(s[i].isdigit()):
                has_int = True
                continue
            else:
                return False
  
        return has_int
