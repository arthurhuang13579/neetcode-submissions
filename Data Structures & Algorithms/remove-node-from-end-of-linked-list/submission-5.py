# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp


        i = 1
        start = prev
        prev = None
        while start:
            if i == n:
                if not start.next:
                    start.next = None
                    break
                start = start.next
            temp = start.next
            start.next = prev
            prev = start
            start = temp 
            i += 1

        return prev




        