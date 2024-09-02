# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node,s, start):
            if not node: return 
            s-=node.val
            if s==0:self.count+=1
            
            dfs(node.left, s, False)
            dfs(node.right, s, False)
            if start:
                dfs(node.left, targetSum, True)
                dfs(node.right, targetSum, True) 
        dfs(root, targetSum, True)
        return self.count        