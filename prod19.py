from typing import Optional
from python.prod876 import ListNode 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for i in range(n):
            fast = fast.next
            if fast is None:
                return None
        return fast

if __name__ == '__main__':
    head = ListNode.from_list([1,2,3,4,5])
