class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = 1
        best = ""
        charcounts = {c: 0 for c in t}
        for c in t:
            charcounts[c] += 1
        seen = defaultdict(int)
        seen[s[start]] += 1
        while True:
            # print(start, end, s[start:end], seen)
            if end > len(s) or start >= len(s):
                return best
            if s[start] not in charcounts:
                seen[s[start]] -= 1
                start += 1
                continue
            allSeen = all([
                count <= seen[c]
                for c, count in charcounts.items()
            ])
            if allSeen:
                if best == "" or end - start < len(best):
                    best = s[start:end]
                seen[s[start]] -= 1
                start += 1
            else:
                end += 1
                if end <= len(s):
                    seen[s[end - 1]] += 1
