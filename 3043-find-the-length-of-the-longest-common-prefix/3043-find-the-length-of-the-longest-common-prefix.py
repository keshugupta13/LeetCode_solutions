class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        mp={}
        for num in arr1:
            num_str = str(num)
            prefix=""
            for ch in num_str:
                prefix += ch
                if prefix not in mp:
                    mp[prefix] = 1
                else:
                    mp[prefix] += 1
        
        max_len = 0
        for num in arr2:
            num_str = str(num)
            prefix = ""
            for ch in num_str:
                prefix += ch
                if prefix in mp:
                    max_len = max(max_len, len(prefix))
        return max_len
