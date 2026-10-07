# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current=head
        while current!=None and current.next!=None:
            j=current.next
            if current.val==j.val:
                current.next=current.next.next
            else:
                current=current.next
        return head