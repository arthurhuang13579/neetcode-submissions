# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        head = None
        start = None
        pointer_i = list1
        pointer_j = list2
        

        while pointer_i and pointer_j:

            if pointer_i.val <= pointer_j.val:
                if not start:
                    start = pointer_i
                    head = start
                    pointer_i = pointer_i.next
                    continue
                start.next = pointer_i
                start = start.next
                pointer_i = pointer_i.next 
            else:
                if not start:
                    start = pointer_j
                    head = start
                    pointer_j = pointer_j.next
                    continue
                start.next = pointer_j
                start = start.next
                pointer_j = pointer_j.next

        while pointer_i:
            if not start:
                start = pointer_i
                head = start
                pointer_i = pointer_i.next
                continue
            start.next = pointer_i
            start = start.next
            pointer_i = pointer_i.next 
        
        while pointer_j:
            if not start:
                start = pointer_j
                head = start
                pointer_j = pointer_j.next
                continue
            start.next = pointer_j
            start = start.next
            pointer_j = pointer_j.next 

        return head
        
        



    
            



        