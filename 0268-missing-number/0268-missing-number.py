class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[j]==i:
        #             break
        # return i
        sum1=sum(nums)
        sum2=len(nums)*(len(nums)+1)/2
        return int(sum2-sum1)