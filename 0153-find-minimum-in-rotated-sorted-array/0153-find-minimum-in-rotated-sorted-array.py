class Solution(object):
    def findMin(self, nums):
        n=len(nums)
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                return nums[i]
            if i==n-1:
                return nums[0]

        