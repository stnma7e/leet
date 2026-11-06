class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        distances = defaultdict(int)
        for i in range(len(s)):
            d = (ord(t[i]) - ord(s[i])) % 26
            if d == 0:
                continue
            distances[d] += 1

        # print(distances)
        for d, count in distances.items():
            # print(sum([d + 26 * j for j in range(count)]), [d + 26 * j for j in range(count)])
            if d + 26 * (count - 1) > k:
                return False
        return True

        distances = [
            (t_ord[i] - s_ord[i]) % 26
            for i in range(len(s))
            if (t_ord[i] - s_ord[i]) % 26 != 0
        ]
        distances.sort()
        # print(distances)

        if k > 26 * len(distances):
            return True

        first_half = distances
        second_half = []
        first = True
        while first or second_half:
            first = False
            distances = first_half + second_half
            # print(distances)
            first_half = []
            second_half = []
            for i in range(len(distances)):
                # print(distances[i], first_half, second_half)
                if i > 0 and distances[i] == distances[i - 1]:
                    second_half.append(distances[i] + 26)
                else:
                    first_half.append(distances[i])
        distances = first_half + second_half

    
        # print(distances)
        for i in range(len(distances)):
            if distances[i] == 0:
                continue
            if distances[i] > k:
                return False
            if i > 0 and distances[i] == distances[i - 1]:
                return False

        return True
        
