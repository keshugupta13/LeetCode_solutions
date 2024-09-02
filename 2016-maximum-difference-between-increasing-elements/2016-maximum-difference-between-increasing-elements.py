class Solution(object):
    def maximumDifference(self, nums):
        sub = nums[0]
        ans = -1
        for i in range(1,len(nums)):
            ans = max(ans,(nums[i]-sub))
            sub = min(sub,nums[i])
        if ans:
            return ans
        else:
            return -1


        """
        :type nums: List[int]
        :rtype: int
        """
        