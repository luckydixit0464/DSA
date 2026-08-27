class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        se=set(nums)
        ma=0
        for i in se:
            if i-1 not in se:
                lent=1
                cure=i
                while cure+1 in se:
                  cure+=1
                  lent+=1
                ma=max(lent,ma)
        return ma
            
