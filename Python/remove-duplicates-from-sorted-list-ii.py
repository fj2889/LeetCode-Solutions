from __future__ import print_function
# Time:  O(n)
# Space: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.next.val == cur.val:
                val = cur.val;
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = cur
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        return dummy.next

if __name__ == "__main__":
    head, head.next, head.next.next = ListNode(1), ListNode(2), ListNode(3)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(4)
    head.next.next.next.next.next, head.next.next.next.next.next.next = ListNode(4), ListNode(5)
    print(Solution().deleteDuplicates(head))


