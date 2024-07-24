class Solution(object):
    def sortJumbled(self, mapping, nums):
        def translate_integer(num):
                if num == 0:
                    return mapping[0]
                else:        
                    res = 0
                    powerof10 = 1
                    while num > 0:
                        digit = num%10
                        num =  num // 10
                        res = mapping[digit] * powerof10 + res
                        powerof10 *= 10
                    return res

        number_mapping = {}
        for num in nums:
            number_mapping[num] = translate_integer(num)
        nums.sort(key=lambda val: number_mapping[val])
        return nums

        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        