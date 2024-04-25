class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = low +(high-low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
                
        return -1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        