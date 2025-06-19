# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Compute the length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Adjust k
        k %= length
        if k == 0:
            return head
        
        # Step 3: Find new tail (length - k - 1 steps from head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # Step 4: Setup new head and break the list
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head  # Connect old tail to old head

        return new_head

