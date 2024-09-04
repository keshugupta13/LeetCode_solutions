class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        count = 0
        result = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
                result = max(result,count)
            else:
                count = 0
        return result