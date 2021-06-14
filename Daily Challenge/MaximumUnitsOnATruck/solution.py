class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1], reverse = True)
        ans = 0
        box_in = 0
        ind = 0
        n = len(boxTypes)

        while(box_in < truckSize and ind < n):
            num = min(truckSize-box_in, boxTypes[ind][0])
            ans += boxTypes[ind][1]*num
            box_in += num
            ind += 1
            
        return ans
