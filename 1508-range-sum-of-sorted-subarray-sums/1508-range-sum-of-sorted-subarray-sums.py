class Solution(object):
    def rangeSum(self, nums, n, left, right):
        MOD = 10 ** 9 + 7
        arr = []
        
        for i in range(n):
            sum1 = 0
            for j in range(i,n):
                sum1 += nums[j]
                arr.append(sum1)
            
        arr.sort()

        sum2 = sum(arr[left-1:right])
        return sum2 % MOD
         

        