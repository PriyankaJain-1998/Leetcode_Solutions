"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ele = []
        def dfs(node):
            if not node: return 0
            ele.append(node.val)
            for child in node.children: dfs(child)
        dfs(root)
        return ele