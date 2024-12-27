class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        prev = values[0]
        for j in range(1,len(values)):
            ans = max(ans,prev+values[j] - j)
            prev = max(prev, values[j] + j)
        return ans
        