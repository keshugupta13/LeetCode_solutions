class Solution(object):
    def rangeSum(self, nums, n, left, right):
        MOD = 10 ** 9 + 7
        arr = []
        i = 0
        while i < n:
            prefix = 0
            for j in range(i,n):
                prefix += nums[j]
                arr.append(prefix)
            i += 1
        arr.sort()

        sum1 = sum(arr[left-1:right])
        return sum1 % MOD
         

        