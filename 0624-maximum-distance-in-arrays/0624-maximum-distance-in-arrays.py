class Solution(object):
    def maxDistance(self, arrays):
        min_value = arrays[0][0]
        max_value = arrays[0][-1]
        max_diff = 0

        for i in range(1,len(arrays)):
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]

            max_diff = max(max_diff, abs(curr_max - min_value))
            max_diff = max(max_diff, abs(curr_min - max_value))

            min_value = min(min_value,curr_min)
            max_value = max(max_value,curr_max)

        return max_diff

        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        