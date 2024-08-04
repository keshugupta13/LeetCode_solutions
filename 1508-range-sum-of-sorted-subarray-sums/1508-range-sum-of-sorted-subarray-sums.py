class Solution(object):
    def rangeSum(self, nums, n, left, right):
        MOD = 10 ** 9 + 7
        arr = []
        
        for i in range(n):
            prefix = 0
            for j in range(i,n):
                prefix += nums[j]
                arr.append(prefix)
            
        arr.sort()

        sum1 = sum(arr[left-1:right])
        return sum1 % MOD
         

        