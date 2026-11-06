

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        count = 0
        start = 0
        end = 1

        while start < end and end <= len(nums):
            ###
            # partial solution. this exceeds time limit
            ###
            s = sum(nums[start:end]) * (end - start)
            # print(start, end, nums[start:end], s)
            if s < k:
                count += 1
                end += 1
                if end > len(nums):
                    start += 1
                    end = start + 1
            else:
                start += 1
                end = start + 1
        return count


