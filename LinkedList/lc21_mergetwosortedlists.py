# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        result = head
        
        while l1 and l2:
            if l1.val >= l2.val:
                head.next = ListNode(l2.val)
                l2 = l2.next
            else:
                head.next = ListNode(l1.val)
                l1 = l1.next
            head = head.next
        head.next = l1 or l2
        return result.next
        
