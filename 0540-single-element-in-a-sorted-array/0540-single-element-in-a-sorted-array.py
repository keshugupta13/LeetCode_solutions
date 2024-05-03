class Solution(object):
    def singleNonDuplicate(self, nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high - low) // 2 + low
            prev = mid - 1
            nxt = mid + 1
                
            if nums[mid] != nums[prev] and nums[mid] != nums[nxt]:
                return nums[mid]
            elif mid % 2 == 0:
                if nums[prev] == nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[prev] == nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return 0

