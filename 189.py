class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # x = [nums[(i-k) % len(nums)] for i in range(len(nums))]
        # for i in range(len(nums)):
        #     nums[i] = x[i]
        # return

        # for i in range(k):
        #     new = nums[0]
        #     old = None
        #     for j in range(1, len(nums)):
        #         old = nums[j]
        #         nums[j] = new
        #         new = old
        #     nums[0] = new
        # return

        if k == 0:
            return
        i = 0
        new = [0 for j in range(k)]
        for j in range(k):
            new[j] = nums[(len(nums) - k + j) % len(nums)]
        old = None
        while True:
            if i >= len(nums):
                return
            old = [0 for j in range(k)]
            for j in range(k):
                old[j] = nums[(i + j) % len(nums)]
            for j in range(len(new)):
                nums[(i + j) % len(nums)] = new[j]
            new = old
            i += k
