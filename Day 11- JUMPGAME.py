class Solution:
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        if nums[0] == 0:
            return -1

        max_reach = nums[0]
        step = nums[0]
        jump = 1

        for i in range(1, n):
            if i == n - 1:
                return jump

            max_reach = max(max_reach, i + nums[i])
            step -= 1

            if step == 0:
                jump += 1
                if i >= max_reach:
                    return -1
                step = max_reach - i

        return -1

