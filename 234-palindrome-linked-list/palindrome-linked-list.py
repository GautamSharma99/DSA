# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reversell(self,head):
        if head is None or head.next is None:
            return head
        new_head=self.reversell(head.next)
        front=head.next
        front.next=head
        head.next=None
        return new_head




    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        fast=head
        slow=head
        while fast.next and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next

        new_head=self.reversell(slow.next)
        first=head
        second=new_head

        while second is not None:
            if first.val!=second.val:
                
                return False
            first=first.next
            second=second.next

       
        return True


        