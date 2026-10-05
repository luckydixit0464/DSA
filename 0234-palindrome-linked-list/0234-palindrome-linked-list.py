# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        arr=[]
        current=head
        while current:
            arr.append(current.val)
            current=current.next
        i=0
        j=len(arr)-1
        for i in range(len(arr)):
            if arr[i]!=arr[j]:
                return False
            i+=1
            j-=1
        return True