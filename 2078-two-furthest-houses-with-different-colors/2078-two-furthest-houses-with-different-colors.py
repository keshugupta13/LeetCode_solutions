class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        clr1 = colors[0]
        clr2 = colors[-1]
        maxi = 0
        for i in range(n-1,-1,-1):
            if clr1 != colors[i]:
                maxi = max(maxi,i)
                break
        for i in range(n):
            if clr2 != colors[i]:
                maxi = max(maxi,len(colors)-i-1)
                break
        return maxi


