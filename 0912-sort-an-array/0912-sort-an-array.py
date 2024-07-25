class Solution(object):
    def mergeprocedure(self, nums, i, mid, j):
        n1 = mid - i + 1
        n2 = j - mid

        Lsubarray = [0] * n1
        Rsubarray = [0] * n2

        for m in range(n1):
            Lsubarray[m] = nums[i + m]
        for n in range(n2):
            Rsubarray[n] = nums[mid + 1 + n]

        p = 0
        q = 0
        k = i
        while p < n1 and q < n2:
            if Lsubarray[p] <= Rsubarray[q]:
                nums[k] = Lsubarray[p]
                p += 1
            else:
                nums[k] = Rsubarray[q]
                q += 1
            k += 1

        while p < n1:
            nums[k] = Lsubarray[p]
            p += 1
            k += 1

        while q < n2:
            nums[k] = Rsubarray[q]
            q += 1
            k += 1

    def mergesort(self, nums, i, j):
        if i < j:
            mid = i + (j - i) // 2
            self.mergesort(nums, i, mid)
            self.mergesort(nums, mid + 1, j)
            self.mergeprocedure(nums, i, mid, j)
        return nums

    def sortArray(self, nums):
        if len(nums) == 0:
            return []
        return self.mergesort(nums, 0, len(nums)-1)