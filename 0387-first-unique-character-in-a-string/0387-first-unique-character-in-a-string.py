class Solution(object):
    def firstUniqChar(self, s):
        mapping = {}
        for i in s:
            if i in mapping:
                mapping[i] += 1
            else:
                mapping[i] = 1
        for index,char in enumerate(s):
            if mapping[char] == 1:
                return index
        return -1


        """
        :type s: str
        :rtype: int
        """
        