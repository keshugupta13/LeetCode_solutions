class Solution(object):
    def canBeEqual(self, target, arr):
        if len(target) != len(arr):
            return False

        target_count = {}
        arr_count = {}

        for num in target:
            if num in target_count:
                target_count[num] += 1
            else:
                target_count[num] = 1

    
        for num in arr:
            if num in arr_count:
                arr_count[num] += 1
            else:
                arr_count[num] = 1

        if target_count == arr_count:
            return True
        else:
            return False
        