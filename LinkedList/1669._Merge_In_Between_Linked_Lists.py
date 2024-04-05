# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1669. Merge In Between Linked Lists
You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

Build the result list and return its head.

'''
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i= 0
        curr = list1

        while i<a-1:
            curr = curr.next
            i+=1

        head = curr
        while i<=b:
            curr = curr.next
            i+=1

        head.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = curr
        return list1
            


        
