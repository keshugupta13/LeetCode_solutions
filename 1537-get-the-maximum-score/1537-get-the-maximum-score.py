class Solution(object):
    def maxSum(self, arr1, arr2):
        n = len(arr1)
        m = len(arr2)
        i, j = 0, 0
        sum1, sum2 = 0, 0
        ans = 0
        MOD = 10 ** 9 + 7

        while i < n and j < m:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
            else:
                ans += max(sum1, sum2) + arr1[i]
                i += 1
                j += 1
                sum1, sum2 = 0, 0

        while i < n:
            sum1 += arr1[i]
            i += 1

        while j < m:
            sum2 += arr2[j]
            j += 1

        ans += max(sum1, sum2)
        return ans % MOD
        