class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        windowSize = len("".join(words))
        longestWord = max([len(w) for w in words])
        wordSize = len(words[0])
        concatStarts = []
        wordCount = {word: 0 for word in words}
        for word in words:
            wordCount[word] += 1
        for start in range(len(s) - windowSize + 1):
            # window = s[start:start + windowSize]

            foundWords = defaultdict(int)
            for word_idx in range(len(words)):
                word = s[start + word_idx * wordSize:start + (word_idx + 1) * wordSize]
                # print(start, word_idx, word, foundWords)
                if word in wordCount:
                    if foundWords[word] > wordCount[word]:
                        break
                    foundWords[word] += 1
            allWordsFound = all([
                count == foundWords[w]
                for w, count in wordCount.items()
            ])
            if allWordsFound:
                concatStarts.append(start)

            continue


            # this method handles variable length words, but fails the last efficiency test case for fixed length words
            # we can just do a sliding window of size wordSize to fix that so that we don't have to add character by character
            windowStr = []
            foundWords = {word: 0 for word in words}
            for c in window:
                # print(start, "".join(windowStr), foundWords)
                windowStr.extend(c)
                if len(windowStr) > longestWord:
                    break
                word = "".join(windowStr)
                if word in wordCount:
                    if foundWords[word] >= wordCount[word]:
                        break
                    windowStr = []
                    foundWords[word] += 1
            if all([
                count == wordCount[w]
                for w, count in foundWords.items()
            ]):
                concatStarts.append(start)
        
        return concatStarts
