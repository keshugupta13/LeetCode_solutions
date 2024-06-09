class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        s = set()
        answer = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                s.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        for num in s:
            answer.append(num)
        
        return answer
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        