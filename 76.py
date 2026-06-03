class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = 1
        best = ""
        charcounts = {c: 0 for c in t}
        for c in t:
            charcounts[c] += 1
        while True:
            # print(start, end, s[start:end])
            if end > len(s) or start >= len(s):
                return best
            if s[start] not in t:
                start += 1
                continue
            seen = defaultdict(int)
            for c in s[start:end]:
                if c in charcounts:
                    seen[c] += 1
            allSeen = all([
                count <= seen[c]
                for c, count in charcounts.items()
            ])
            # print(seen)
            if allSeen:
                if best == "" or end - start < len(best):
                    best = s[start:end]
                start += 1
            else:
                end += 1
