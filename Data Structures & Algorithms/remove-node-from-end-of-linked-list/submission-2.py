# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = dummy
        
        # 2. Move 'right' pointer n steps ahead
        for _ in range(n):
            right = right.next
            
        # 3. Move both pointers until 'right' hits the end
        while right.next:
            left = left.next
            right = right.next
            
        # 4. Delete the node
        # left is now just before the target node
        left.next = left.next.next
        
        return dummy.next