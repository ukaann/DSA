# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1 is not None:
                val1 = l1.val
            else:
                val1 = 0
            if l2 is not None: 
                val2 = l2.val
            else:
                val2 = 0
            
            total = val1 + val2 + carry
            carry = total//10

            current.next = ListNode(total%10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next