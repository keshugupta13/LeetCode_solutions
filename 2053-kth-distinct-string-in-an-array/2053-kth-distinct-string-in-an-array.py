class Solution(object):
    def kthDistinct(self, arr, k):
        mapping = {}
        for i in arr:
            if i in mapping:
                mapping[i] += 1
            else:
                mapping[i] = 1
        nums = []
        for i in arr:
            if mapping[i] == 1:
                k -= 1
            if k == 0:
                return i
            
        return ""


        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        