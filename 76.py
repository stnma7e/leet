from collections import Counter

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


"""
Using Counter instead of rolling our own dict
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = 1
        best = ""
        charcounts = {c: 0 for c in t}
        for c in t:
            charcounts[c] += 1
        needed = Counter(t)
        if s[start] in charcounts:
            needed.subtract([s[start]])
        while True:
            # print(start, end, s[start:end], needed)
            if start >= len(s):
                return best
            if s[start] not in charcounts:
                start += 1
                continue
            if (+needed).total() == 0:
                if best == "" or end - start < len(best):
                    best = s[start:end]
                if s[start] in charcounts:
                    needed.update([s[start]])
                start += 1
            else:
                if end != len(s):
                    end += 1
                    newchar = s[end - 1]
                    if newchar in charcounts:
                        needed.subtract([s[end - 1]])
                else:
                    if s[start] in charcounts:
                        needed.update([s[start]])
                    start += 1

