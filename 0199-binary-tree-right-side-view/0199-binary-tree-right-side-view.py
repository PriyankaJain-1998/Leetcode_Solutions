# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ele = []
        def dfs(node, level): 
            if not node: return 
            if len(ele)>level: ele[level]= node.val
            else: ele.append(node.val)

            dfs(node.left,level+1)
            dfs(node.right,level+1)
            # ele.append(node.val)

        dfs(root, 0)
        return ele
        