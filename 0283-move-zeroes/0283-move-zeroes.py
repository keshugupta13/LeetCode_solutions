class Solution(object):
    def moveZeroes(self, arr):
        n = len(arr)
        j = -1
        for i in range(n):
            if arr[i] == 0:
                j = i
                break
        
        for i in range(j+1,n):
            if arr[i] != 0:
                arr[j],arr[i] = arr[i],arr[j]
                j += 1

        return arr
        