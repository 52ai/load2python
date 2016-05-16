class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
  
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0; head = ListNode(0); curr = head;
        while l1 and l2:
            Sum = l1.val + l2.val + carry
            carry = Sum / 10
            curr.next = ListNode(Sum % 10)
            l1 = l1.next; l2 = l2.next; curr = curr.next
        while l1:
            Sum = l1.val + carry
            carry = Sum / 10
            curr.next = ListNode(Sum % 10)
            l1 = l1.next; curr = curr.next
        while l2:
            Sum = l2.val + carry
            carry = Sum / 10
            curr.next = ListNode(Sum % 10)
            l2 = l2.next; curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next
 
# how to test
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
hellohello = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = hellohello.addTwoNumbers(l1, l2)
p = result
while p:
    print p.val, '->',
    p = p.next
