# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0

        depth = 1
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                root = queue.pop(0)

                if root.left is None and root.right is None:
                    return depth

                if root.left is not None:
                    queue.append(root.left)

                if root.right is not None:
                    queue.append(root.right)

            depth  += 1
        return depth

            



        """
        :type root: TreeNode
        :rtype: int
        """
        