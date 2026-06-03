class Solution:
    def candy(self, ratings: List[int]) -> int:
        assignments = [1 for i in ratings]
        if len(ratings) <= 1:
            return sum(assignments)
        while True:
            # this works, but is not efficient for large values of ratings
            all_good = True
            for i in range(len(assignments)):
                # print(assignments)
                left = 0 if i == 0 else assignments[i - 1]
                right = 0 if i + 1 >= len(assignments) else assignments[i + 1]
                cur = assignments[i]
                if ratings[i] > ratings[i - 1] and cur <= left or ratings[i] > ratings[(i + 1) % len(ratings)] and cur <= right:
                    # print(i, cur, left, right)
                    assignments[i] += 1
                    all_good = False
            if all_good:
                return sum(assignments)
