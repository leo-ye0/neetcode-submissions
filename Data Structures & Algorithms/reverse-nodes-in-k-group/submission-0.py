# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Check if there are k nodes to reverse
        curr = head
        for _ in range(k):
            if not curr:
                return head  # Not enough nodes, return head as-is
            curr = curr.next

        # 2. Reverse k nodes (standard linked list reversal)
        prev = None
        curr = head
        for _ in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # 3. Connect: head is now the TAIL of this group.
        # Its next should be the head of the NEXT reversed group.
        head.next = self.reverseKGroup(curr, k)

        # 4. Return prev (the NEW HEAD of this reversed group)
        return prev