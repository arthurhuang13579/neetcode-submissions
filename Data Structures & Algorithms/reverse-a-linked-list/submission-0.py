# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            #print("Curr val: " + str(curr.val))
            temp = curr.next
            #print("Next val: " + str(temp.val))
            #print("Previous val: " + str(prev.val))
            curr.next = prev
            #print("Value is linked to: " + str(curr.next.val))
            prev = curr
            curr = temp
        return prev
    
        
