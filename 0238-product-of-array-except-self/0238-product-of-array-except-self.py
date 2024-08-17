class Solution(object):
    def productExceptSelf(self, nums):
        product = 1
        count_0 = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                count_0 += 1
            else:
                product *= nums[i]

        for i in range(n):
            if count_0 > 1:
                nums[i] = 0

            elif count_0 == 0:
                nums[i] =  product // nums[i]
            
            elif count_0 == 1 and nums[i] != 0:
                nums[i] = 0

            else:
                nums[i] = product
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        