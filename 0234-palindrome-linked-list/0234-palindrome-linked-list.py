# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        # arr=[]
        # current=head
        # while current:
        #     arr.append(current.val)
        #     current=current.next
        # i=0
        # j=len(arr)-1
        # for i in range(len(arr)):
        #     if arr[i]!=arr[j]:
        #         return False
        #     i+=1
        #     j-=1
        # return True
        #optimised
        slow = head
        fast = head

# Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

# Reverse second half
        prev = None
        cur = slow

        while cur:
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t

# Compare both halves
        p1 = head
        p2 = prev

        while p2:
            if p1.val != p2.val:
                return False

            p1 = p1.next
            p2 = p2.next

        return True
            

            
