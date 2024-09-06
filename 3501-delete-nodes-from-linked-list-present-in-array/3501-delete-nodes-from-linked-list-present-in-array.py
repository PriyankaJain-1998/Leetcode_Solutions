# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)        
        
        while head.val in nums:                 # <-- 1)
            head = head.next

        ans = ListNode(head.val, head)          # <-- 2)
 
        while head and head.next:               # <-- 3)
            if head.next.val in nums:
                head.next = head.next.next

            else:                               # <-- 4)
                head = head.next

        return ans.next                         # <-- 5)