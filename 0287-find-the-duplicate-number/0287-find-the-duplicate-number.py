class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        dup=set()
        for i in range(len(nums)):
            if nums[i] not in dup:
                dup.add(nums[i])
            elif nums[i] in dup:
                return nums[i]
            else:
                return False