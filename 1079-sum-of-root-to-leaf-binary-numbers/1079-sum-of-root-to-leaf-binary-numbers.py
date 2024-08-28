# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = 0
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        paths = []
        def dfs(node, path):
            if not node: return 
            path.append(str(node.val))

            if not node.left and not node.right:
                paths.append(int(''.join(path.copy()),2))
            else:
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)

            path.pop()

        dfs(root, [])
        return sum(paths)