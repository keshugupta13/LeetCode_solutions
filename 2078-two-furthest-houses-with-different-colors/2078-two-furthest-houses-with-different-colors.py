class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        clr1 = colors[0]
        clr2 = colors[-1]
        maxi1 = 0
        maxi2 = 0
        for i in range(n-1,-1,-1):
            if clr1 != colors[i]:
                maxi1 = max(maxi1,i)
                break
        for i in range(n):
            if clr2 != colors[i]:
                maxi2 = max(maxi2,len(colors)-i-1)
                break
        return max(maxi1,maxi2)


