# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorder(self,root,ans):
        if root is None:
            return
        
        self.postorder(root.left,ans)
        self.postorder(root.right,ans)
        ans.append(root.val)

    def postorderTraversal(self, root):
        ans = []
        self.postorder(root,ans)
        return ans

        """
        :type root: TreeNode
        :rtype: List[int]
        """
        