# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur_idx, data, output =0, {}, 0
        cur_node = head

        ## will give me the total number of nodes present in the linked list
        while cur_node.next:
            data[cur_idx]=cur_node.val
            cur_node=cur_node.next
            cur_idx+=1
            
        data[cur_idx]=cur_node.val
        cur_idx +=1
        for i in range(int(cur_idx/2)):
            twin_sum = data[i] + data[cur_idx-1-i]
            if twin_sum>output: output = twin_sum

        return output