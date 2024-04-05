# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
114.Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Base condition- return if root is None
        # or if it is a leaf node
        if (root == None or root.left == None and root.right == None): return
        
        # If root.left exists then we have 
        # to make it root.right
        if (root.left != None):
    
            # Move left recursively
            self.flatten(root.left)
        
            # Store the node root.right
            tmpRight = root.right
            root.right = root.left
            root.left = None
    
            # Find the position to insert
            # the stored value   
            t = root.right
            while (t.right != None):
                t = t.right
    
            # Insert the stored value
            t.right = tmpRight
    
        # Now call the same function
        # for root.right
        self.flatten(root.right)


