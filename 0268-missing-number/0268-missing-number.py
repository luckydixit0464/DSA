class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        fount=False
        # for i in range(len(nums)+1):
        #     fount=False
        #     for j in range(len(nums)):
        #         if nums[j]==i:
        #             found=True
        #             break
        #     if not found:
        #        return i

        # sum1=sum(nums)
        # sum2=len(nums)*(len(nums)+1)/2
        # return int(sum2-sum1)
    
        expected=0
        expected1=0
        for i in range(len(nums)):
            expected=expected^nums[i]
        for i in range(len(nums)+1):
            expected1=expected1^i
        return expected^expected1

