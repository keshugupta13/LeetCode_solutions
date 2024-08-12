class Solution(object):
    def findDuplicate(self, nums):
        arr = [0] * (len(nums) + 1)
        duplicate_value = 0
        for num in nums:
            arr[num] += 1
        
        for i in range(1, len(arr)):
            if arr[i] > 1:
                duplicate_value = i
                break  

        return duplicate_value