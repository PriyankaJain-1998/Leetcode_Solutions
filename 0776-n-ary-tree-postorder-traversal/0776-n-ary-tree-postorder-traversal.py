"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if node: 
                for c in node.children:
                    dfs(c)
                ele.append(node.val)
        
        ele = []
        dfs(root)
        return ele
        