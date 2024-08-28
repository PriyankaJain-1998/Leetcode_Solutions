# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ele = []
        def dfs(node):
            # if node: 
            #     if node.left:
            #         ele.append(node.left.val)
            #         dfs(node.left)
            #     dfs(node.right)

            if not node: return 0
            if node.left and not node.left.left and not node.left.right:
                return node.left.val + dfs(node.right) + dfs(node.left)
            # Recursively call dfs on both left and right children
            return dfs(node.left) + dfs(node.right)
        # dfs(root)
        return dfs(root)
        
    