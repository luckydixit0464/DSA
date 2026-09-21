class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # k = k % n

        # def reverse(left, right):
        #     while left < right:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        #         right -= 1

        # reverse(0, n - 1)
        # reverse(0, k - 1)
        # reverse(k, n - 1)
        # return nums
        n = len(nums)
        k = k % n
        i=n-k
        j=0
        temp=[0]*n
        for i in range(n-k,n):
            temp[j]=nums[i]
            j+=1

        for i in range(n-k):
            temp[j]=nums[i]
            j+=1
        for i in range(n):
            nums[i]=temp[i]
        return nums