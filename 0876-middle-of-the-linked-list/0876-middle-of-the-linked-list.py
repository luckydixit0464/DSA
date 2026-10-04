# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        # brute force
        # co=0
        # current =head
        # while current:
        #     co+=1
        #     current=current.next
        # current=head
        # mid=co//2
        # for i in range(mid):
        #     current=current.next
        # return current
        #optimised
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

