class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # ans = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     ans.append(product)
        # return ans
        # optimised
        ans=[1]*len(nums)
        pre=[1]*len(nums)
        suf=[1]*len(nums)
        for i in range(1,len(nums)):
            pre[i]=pre[i-1]*nums[i-1]
        suf[len(nums)-1]=1
        for i in range(len(nums)-2,-1,-1):
            suf[i]=suf[i+1]*nums[i+1]    
        for i in range(len(nums)):
            ans[i]=pre[i]*suf[i]
        return ans    
