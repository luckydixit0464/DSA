class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # for i in range(len(nums)):
        #     lefts=0
        #     rights=0
        #     for j in range(0,i):
        #         lefts+=nums[j]
        #     for j in range(i+1,len(nums)):
        #         rights+=nums[j]
        #     if lefts==rights:
        #         return i
        # return -1
        # optimised
        total=0
        for i in range(len(nums)):
            total+=nums[i]
        ls=0
        rs=0
        for i in range(len(nums)):
            rts=total-ls-nums[i]
            if ls==rts:
                return i
            ls+=nums[i]
        return -1