# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diff= 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, minValue, maxValue):
            if not node: return 
            minValue = min(minValue, node.val)
            maxValue = max(maxValue, node.val)

            self.diff = max(self.diff, maxValue-minValue)
            dfs(node.left, minValue, maxValue)
            dfs(node.right, minValue, maxValue)

        dfs(root,root.val, root.val)
        return self.diff