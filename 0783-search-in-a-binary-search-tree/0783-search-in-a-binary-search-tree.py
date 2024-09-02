# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return 0
            if node.val == val:return node
            if node.left: 
                left = dfs(node.left)
                if left: return left
            if node.right: 
                right = dfs(node.right)
                if right: return right
            return None
        return dfs(root) 