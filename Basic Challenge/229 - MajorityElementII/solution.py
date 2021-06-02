class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2 = 0, 0
        cand1, cand2 = None, None
        
        for num in nums :
            if(count1 > 0 and count2 > 0):
                if(cand1 == num):
                    count1+=1
                elif(cand2 == num):
                    count2+=1
                else:
                    count1-=1
                    count2-=1
                
            elif(count1 > 0):
                if(cand1 == num):
                    count1+=1
                else:
                    cand2=num
                    count2+=1
            
            elif(count2 > 0):
                if(cand2 == num):
                    count2+=1
                else:
                    cand1=num
                    count1+=1
                    
            else:
                cand1 = num
                count1 += 1
                
        count1, count2 = 0, 0
        for num in nums:
            count1 += (num == cand1)
            count2 += (num == cand2)
            
        ans = []
        if(3*count1 > len(nums)):
            ans.append(cand1)
                
        if(3*count2 > len(nums) and cand1 != cand2):
            ans.append(cand2)
    
        return ans
