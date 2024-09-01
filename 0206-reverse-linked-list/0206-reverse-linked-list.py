# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return

        # ele =[]
        # def dfs(node):
        #     if not node: return
        #     dfs(node.next)
        #     ele.append(node.val)

        # dfs(head)

        # cur = dummy = ListNode(0)
        # for e in ele:
        #     cur.next = ListNode(e)
        #     cur = cur.next
        # return dummy.next    

        cur = head
        prev = None
        while cur:
            nxt = cur.next 
            cur.next = prev
            prev, cur = cur, nxt
        return prev