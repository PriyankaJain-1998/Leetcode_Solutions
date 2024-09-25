# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, target):
            if not node: return 
            left_sum = dfs(node.left, target-node.val)
            right_sum = dfs(node.right, target-node.val)
            if not node.left and not node.right: 
                return target == node.val

            return left_sum or right_sum
            
        return dfs(root, targetSum)
        
            