class Solution(object):
    def moveZeroes(self, arr):
        n = len(arr)
        count = 0
        for i in range(n):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1

        while count < n:
            arr[count] = 0
            count += 1
        return arr