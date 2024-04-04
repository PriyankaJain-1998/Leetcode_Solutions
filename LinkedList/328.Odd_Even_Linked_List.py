'''
Given the head of a singly linked list, group all the nodes with odd indices 
together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
'''
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: return head

        oddptr = current = head
        evenptr = evenhead = head.next
        i = 1
        while current:
            if i>2 and i%2!=0:
                oddptr.next = current 
                oddptr = oddptr.next

            elif i>2 and i%2==0:
                evenptr.next = current 
                evenptr = evenptr.next
            current = current.next
            i +=1

        evenptr.next = None
        oddptr.next = evenhead

        return head

