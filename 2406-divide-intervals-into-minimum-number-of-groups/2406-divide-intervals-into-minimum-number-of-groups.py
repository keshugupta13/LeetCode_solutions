class Solution(object):
    def minGroups(self, intervals):
        n = len(intervals)
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        group = 1
        ans = 1
        i,j = 1,0
        while i < n and j<n:
            if start_times[i] <= end_times[j]:
                group += 1
                i += 1
            else:
                group -= 1
                j += 1

            ans = max(ans,group)
        return ans