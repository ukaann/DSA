# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        bal = 0
        res = ListNode()
        tes = res
        while l1 and l2:
            s = l1.val + l2.val + bal
            bal = 0
            if (s >= 10):
                bal = 1
                s %= 10
            tes.next = ListNode(s)
            l1 = l1.next
            l2 = l2.next
            tes = tes.next
        while l1:
            s = l1.val + bal
            bal = 0
            if (s >= 10):
                bal = 1
                s %= 10
            tes.next = ListNode(s)
            l1 = l1.next
            tes = tes.next
        while l2:
            s = l2.val + bal
            bal = 0
            if (s >= 10):
                bal = 1
                s %= 10
            tes.next = ListNode(s)
            l2 = l2.next
            tes = tes.next
        if bal == 1:
            tes.next = ListNode(bal)
        return res.next