class Solution(object):
    def divideArray(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        return all(count % 2 == 0 for count in freq.values())


        

        
        """
        :type nums: List[int]
        :rtype: bool
        """
        