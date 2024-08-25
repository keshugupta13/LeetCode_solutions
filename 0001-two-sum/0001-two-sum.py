class Solution(object):
    def twoSum(self, nums, target):
        mp = {}
        for i in range(len(nums)):
            num = nums[i]
            remtarget = target - num
            if remtarget in mp:
                return [mp[remtarget], i]
            mp[num] = i
        return []