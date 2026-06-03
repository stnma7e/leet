class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_index_used = 0
        for i in range(len(nums)):
            cur = nums[i]
            if (i < len(nums) - 1 and cur != nums[i + 1]) or (i < len(nums) - 2 and cur != nums[i+2]):
                nums[last_index_used] = cur
                last_index_used += 1
            elif i == len(nums) - 1 or i == len(nums) - 2:
                nums[last_index_used] = cur
                last_index_used += 1
        return last_index_used
