class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # if not nums:
        #     return 0
        # k=1
        # for i in range(1,len(nums)):
        #     if nums[i-1]!=nums[i]:
        #         nums[k]=nums[i]
        #         k+=1
        # return k
        i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1
            