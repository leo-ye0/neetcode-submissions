# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # 1. Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # second starts the second half
        second = slow.next
        slow.next = None # 1st half
        
        # 2. Reverse the second half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev
        
        # 3. Interleave the two halves
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            
            first.next = second  # Connect first node to last node
            second.next = tmp1  # Connect last node to second node
            
            first = tmp1        # Advance first pointer
            second = tmp2       # Advance second pointer