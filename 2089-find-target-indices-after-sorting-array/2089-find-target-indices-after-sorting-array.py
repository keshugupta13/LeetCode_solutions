class Solution(object):
    def targetIndices(self, nums, target):
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        return result
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        