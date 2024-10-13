class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i == -1:
            nums.reverse()
            return

        pivot = i

        j = len(nums) - 1
        while nums[j] <= nums[pivot]:
            j -= 1

        nums[pivot], nums[j] = nums[j], nums[pivot]

        nums[pivot + 1:] = reversed(nums[pivot + 1:])
