class Solution(object):
    def findcombination(self, indx, arr, target, current_combination, results):
        if indx >= len(arr):
            return

        if target == 0:
            results.append(list(current_combination))
            return

        if arr[indx] <= target:
            current_combination.append(arr[indx])
            self.findcombination(indx, arr, target - arr[indx], current_combination, results)
            current_combination.pop()

        self.findcombination(indx + 1, arr, target, current_combination, results)

    def combinationSum(self, candidates, target):
        results = []
        self.findcombination(0, candidates, target, [], results)
        return results

        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        