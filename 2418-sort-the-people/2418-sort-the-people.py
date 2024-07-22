class Solution(object):
    def sortPeople(self, names, heights):
        n = len(names)
        mapping = {}
        for i in range(n):
            mapping[heights[i]] = names[i]

        heights.sort(reverse = True)
        for j in range(n):
            h = heights[j]
            names[j] = mapping[h]

        return names








        

        

        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        