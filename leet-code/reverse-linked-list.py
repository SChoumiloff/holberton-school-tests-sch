# using https://thuongthanhto.medium.com/linked-list-reverse-between-98e4fe5c208d


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
            return 
        dummy_node = ListNode(0, head)
        current = dummy_node.next
        prev = dummy_node

        for _ in range(left - 1):
            prev = current
            current = prev.next

        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy_node.next
