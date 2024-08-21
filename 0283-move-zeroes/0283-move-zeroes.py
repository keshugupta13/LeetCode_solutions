class Solution(object):
    def moveZeroes(self, arr):
        idx = 0
        n = len(arr)
        for i in range(n):
            if arr[i] != 0:
                arr[idx] = arr[i]
                idx += 1
        while idx < n:
            arr[idx] = 0
            idx += 1
        
        return arr
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        