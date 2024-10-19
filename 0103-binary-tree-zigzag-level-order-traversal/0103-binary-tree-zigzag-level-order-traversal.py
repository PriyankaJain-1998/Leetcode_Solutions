# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        final_ans = []
        if not root : return ans 
        currentlevel, nextlevel = [],[]
        currentlevel.append(root)
        leftToRight = True
        while currentlevel : 
            size = len(currentlevel)

            while size>0:
                size-=1
                curr = currentlevel.pop()
                ans.append(curr.val)

                if leftToRight: 
                    if curr.left: nextlevel.append(curr.left)
                    if curr.right: nextlevel.append(curr.right)
                else:
                    if curr.right: nextlevel.append(curr.right)
                    if curr.left: nextlevel.append(curr.left)

            leftToRight = not leftToRight
            final_ans.append(ans)
            ans = []
            currentlevel, nextlevel = nextlevel, currentlevel
        return final_ans
                