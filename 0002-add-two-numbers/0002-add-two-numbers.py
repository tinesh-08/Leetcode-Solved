# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        c=0
        res = l3
        while(l1 and l2):
            sum=l1.val+l2.val+c
            c=sum//10
            l3.next=ListNode(sum%10)
            l1=l1.next
            l2=l2.next
            l3=l3.next
        while(l1):
            sum=l1.val+c
            c=sum//10
            l3.next=ListNode(sum%10)
            l1=l1.next
            l3=l3.next
        while(l2):
            sum=l2.val+c
            c=sum//10
            l3.next=ListNode(sum%10)
            l2=l2.next
            l3=l3.next
        if c:
            l3.next=ListNode(c)
        return res.next
        