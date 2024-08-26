# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1, ptr2 = headA, headB
    
        while ptr1 != ptr2:
            # When ptr1 reaches the end, start from the beginning of headB
            ptr1 = ptr1.next if ptr1 else headB
            # When ptr2 reaches the end, start from the beginning of headA
            ptr2 = ptr2.next if ptr2 else headA
        
        return ptr1 