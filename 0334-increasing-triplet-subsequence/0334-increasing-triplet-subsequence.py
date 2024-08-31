class Solution(object):
    def increasingTriplet(self, nums):
        n = len(nums)
        small = [-1] * n
        big = [-1] * n
        small[0] = nums[0]
        for i in range(n):
            small[i] = min(nums[i],small[i-1])

        big[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            big[i] = max(nums[i],big[i+1])

        for i in range(n):
            if nums[i] > small[i] and nums[i] < big[i]:
                return True
        return False      