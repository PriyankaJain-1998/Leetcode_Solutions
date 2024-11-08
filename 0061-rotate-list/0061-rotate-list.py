# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # ele = []
        # def dfs(node):
        #     if not node: return 
        #     ele.append(node.val)
        #     dfs(node.next)
        # dfs(head)
        # if len(ele)==0 or len(ele)==1: return head
        # for i in range(k):
        #     ele = [ele[len(ele)-1]]+ ele[0:len(ele)-1]

        # cur = dummy = ListNode(0)
        # for e in ele:
        #     cur.next = ListNode(e)
        #     cur = cur.next
        # return dummy.next


        if head is None:
            return None

        curr = head
        size = 1

        # calculating length and making a circular loop
        while curr.next is not None:
            curr = curr.next
            size += 1

        curr.next = head

        # cut from the rotating point
        i = size - (k % size)

        while i > 1:
            head = head.next
            i -= 1

        curr = head.next
        head.next = None
        return curr