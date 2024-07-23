from collections import Counter
class Solution(object):
    def frequencySort(self, nums):
        freq = Counter(nums)

        def custom_sort(n):
            return (freq[n] , -n)

        nums.sort(key=custom_sort)
        return nums