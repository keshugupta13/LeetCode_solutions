class Solution(object):
    def subsetXORSum(self, nums):
        bits = 0
        for n in nums:
            bits |= n
        return bits * 2**(len(nums)-1)
        
        