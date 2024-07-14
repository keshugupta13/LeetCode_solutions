class Solution(object):
    def threeSumClosest(self, arr, target):
        arr.sort()
        closest_sum = float('inf')
        closest_diff = float('inf')
        
        for i in range(0, len(arr) - 2):
            j = i + 1
            k = len(arr) - 1
            while j < k:
                sum1 = arr[i] + arr[j] + arr[k]
                diff = abs(sum1 - target)
                if diff < closest_diff:
                    closest_diff = diff
                    closest_sum = sum1
                if sum1 == target:
                    return target
                elif sum1 < target:
                    j += 1
                else:
                    k -= 1
        
        return closest_sum

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        