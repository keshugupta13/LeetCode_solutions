class Solution(object):
    def isAnagram(self, s, t):
         if len(s) != len(t):
            return False
    
         dict_s = {}
         dict_t = {}

         for char in s:
             if char in dict_s:
                 dict_s[char] += 1
             else:
                 dict_s[char] = 1
    
         for char in t:
             if char in dict_t:
                 dict_t[char] += 1
             else:
                 dict_t[char] = 1
    

         return dict_s == dict_t