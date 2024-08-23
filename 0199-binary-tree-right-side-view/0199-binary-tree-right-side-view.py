# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        ans = []
        self.right_view(root, ans, 0)
        return ans

    def right_view(self, root, ans, level):
        if root is None:
            return

        if level == len(ans):
            ans.append(root.val)
        self.right_view(root.right, ans, level + 1)
        self.right_view(root.left, ans, level + 1)


        """
        :type root: TreeNode
        :rtype: List[int]
        """
        