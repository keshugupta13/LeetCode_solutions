# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    def setnode(self, low, high, nums):
        if low >= high:
            return None
        
        mid = low + (high - low) // 2
        root = self.TreeNode(nums[mid])
        
        root.left = self.setnode(low, mid, nums)
        root.right = self.setnode(mid + 1, high, nums)
        
        return root
    def sortedArrayToBST(self, nums):
        return self.setnode(0, len(nums), nums)
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        