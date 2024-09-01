# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ele = []
        def dfs(node):
            if not node: return 
            ele.append(node.val)
            dfs(node.next)

        dfs(head)
        del ele[int(len(ele)/2)]

        curr = dummy = ListNode(0)
        for i in ele:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
            
        