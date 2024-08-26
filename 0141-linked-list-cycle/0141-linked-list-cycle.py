# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        head_set = set()

        while head is not None:
            if head in head_set: return True
            head_set.add(head)
            head = head.next
        return False