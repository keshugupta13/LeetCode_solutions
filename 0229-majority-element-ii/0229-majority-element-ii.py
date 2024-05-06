class Solution(object):
    def majorityElement(self, nums):
        n3 = len(nums) // 3
        dic = {}
        arr = []
		
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] = dic[num] + 1
				
        for key in dic:
            if dic[key] > n3:
                arr.append(key)
				
        return arr
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        