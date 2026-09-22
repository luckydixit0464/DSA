class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        co0=0
        co1=0
        co2=0
        for i in range(len(nums)):
            if nums[i]==0:
                co0+=1
            elif nums[i]==1: 
                co1+=1
            elif nums[i]==2:
                co2+=1
        index=0
        while(co0>0):
            nums[index]=0
            co0-=1
            index+=1
        while(co1>0):
            nums[index]=1
            co1-=1
            index+=1
        while(co2>0):
                nums[index]=2
                co2-=1
                index+=1
        return nums
        # low=0
        # mid=0
        # high=len(nums)-1
        # while(mid<=high):
        #     if nums[mid]==0:
        #         nums[mid],nums[low]=nums[low],nums[mid]
        #         low+=1
        #         mid+=1
        #     elif nums[mid]==2:
        #         nums[mid],nums[high]=nums[high],nums[mid]
        #         mid+=1
        #         high-=1
        #     else:
        #         mid+=1
        # return nums
            