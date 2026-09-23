class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        mis=-1
        dup=-1
        # for i in range(1,len(nums)+1):
        #     count=0
        #     for j in range(len(nums)):
        #         if nums[j]==i:
        #             count+=1
        #     if count==0:
        #         mis=i
        #     if count==2:
        #         dup=i
        # return [dup,mis]
        
        fre=[0]*(len(nums)+1)
        for i in range(len(nums)):
            fre[nums[i]]+=1
        for i in range(1,len(fre)):
            if fre[i]==0:
                mis=i
            if fre[i]==2:
                dup=i
        return [dup,mis]