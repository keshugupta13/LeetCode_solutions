class Solution(object):
    def maximumDifference(self, nums):
        maxi = -1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    maxi = max(maxi,abs(nums[i]-nums[j]))

        return maxi
    


        """
        :type nums: List[int]
        :rtype: int
        """
        