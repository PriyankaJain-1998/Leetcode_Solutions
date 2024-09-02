# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxlevel = 0
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        m = defaultdict(list)
        
        def dfs(node, level):
            if not node: return
            
            dfs(node.left, level+1)
            m[level].append(node.val)
            global maxlevel
            maxlevel = max(self.maxlevel, level)
            dfs(node.right,level+1)

        dfs(root,0)
        
        m_sorted = sorted(m)
        print(m_sorted)
        ans = -9999999
        level_sum = -9999999
        for key in m_sorted:
            print("-",key, sum(m[key]),ans)
            if sum(m[key]) > level_sum: 
                level_sum = sum(m[key])
                ans = key
            print(sum(m[key]),ans)
        return ans+1
        
        