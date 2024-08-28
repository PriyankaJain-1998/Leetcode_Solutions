# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ele = []
        def dfs(node):
            if not node: return 
            dfs(node.left)
            ele.append(node.val)
            dfs(node.right)
        dfs(root)
        ele = sorted(list(set(ele)))
        print(ele)
        if len(ele)==1: return -1
        else: return ele[1]