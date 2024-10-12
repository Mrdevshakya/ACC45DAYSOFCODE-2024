class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        left = 0
        sum = 0
        min_length = float('inf')
        
        for right in range(n):
            sum += nums[right]
            
            while sum >= target:
                min_length = min(min_length, right - left + 1)
                sum -= nums[left]
                left += 1
        
        return 0 if min_length == float('inf') else min_length
