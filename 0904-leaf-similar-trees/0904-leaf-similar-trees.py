# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ele = []
        def dfs(node):
            
            if not node: return 
            if not node.left and not node.right:
                ele.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return ele
        
        ele1 = dfs(root1)
        ele = []
        ele2 = dfs(root2)
        if ele1==ele2: return True
        else: return False