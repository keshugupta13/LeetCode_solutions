class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        unique_triplets = set()
        result = []
        n = len(nums)
        for i in range(n-2):
            left, right = i + 1 , n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    unique_triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        for triplet in unique_triplets:
            result.append(list(triplet))
        return result
