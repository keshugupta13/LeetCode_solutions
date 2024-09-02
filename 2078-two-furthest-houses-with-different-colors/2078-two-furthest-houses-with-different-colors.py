class Solution(object):
    def maxDistance(self, colors):
        max_dist = 0
        for i in range(len(colors)-1):
            for j in range(i,len(colors)):
                if colors[i] != colors[j]:
                    curr_diff = j - i
                    max_dist = max(curr_diff,max_dist)
                else:
                    continue
        return max_dist
                