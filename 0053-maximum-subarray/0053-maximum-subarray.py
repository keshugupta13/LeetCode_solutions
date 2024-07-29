class Solution(object):
    def maxSubArray(self, nums):
        max_sum1 = float('-inf')
        sum1 = 0 
        for num in nums:
            sum1 += num
            if sum1 > max_sum1:
                max_sum1 = sum1
            if sum1 < 0:
                sum1 = 0

        return max_sum1


        """
        :type nums: List[int]
        :rtype: int
        """
        