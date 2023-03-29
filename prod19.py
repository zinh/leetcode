from typing import Optional
from python.prod876 import ListNode 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(n + 1):
            if fast is None:
                break
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

if __name__ == '__main__':
    head = ListNode.from_list([1])
    s = Solution()
    # import pdb; pdb.set_trace()
    head = s.removeNthFromEnd(head, 1)
    print(list(head))
