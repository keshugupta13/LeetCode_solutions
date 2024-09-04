class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        i = 0
        j = n-1
        while colors[i] == colors[n-1]:
            i += 1
        max1 = abs(n-1-i)

        while colors[j] == colors[0]:
            j -= 1
        max2 = abs(0-j)
        return max(max1,max2)



