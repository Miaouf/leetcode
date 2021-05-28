class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        total = 0
        ans = 0
        start = 0
        
        for num in nums:
            dic[num] += 1
            total += num
            while(dic[num] > 1):
                dic[nums[start]] -= 1
                total -= nums[start]
                start += 1
            ans = max(total,ans)
        return ans
                
