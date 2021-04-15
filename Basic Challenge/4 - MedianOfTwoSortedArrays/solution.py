class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        n = len(nums1)
        if(len(nums1)%2 == 1):
            return nums1[int(n/2)]
        else:
            return (nums1[int(n/2)-1]+nums1[int(n/2)])/2
