from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, lst):
        if not lst:
            return None

        head = cls(lst[0])
        previous = head
        for item in lst[1:]:
            node = ListNode(item)
            previous.next = node
            previous = node
        return head

    def __iter__(self):
        self.head = self
        return self

    def __next__(self):
        if self.head is None:
            raise StopIteration
        else:
            value = self.head.val
            self.head = self.head.next
            return value

class Solution:
    def traverse(self, node, depth):
        if node:
            middle = self.traverse(node.next, depth + 1)
            if isinstance(middle, int):
                if middle == depth:
                    return node
            return middle
        else:
            return depth // 2

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.traverse(head, 0)

class Solution2:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Use a slow and a fast pointer that travel twice as fast as slow pointer
        '''
        fast, slow = head, head
        if fast is None:
            return None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

if __name__ == "__main__":
    s = Solution2()
    head = ListNode.from_list([1])
    print(s.middleNode(head).val)
