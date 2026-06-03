class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wordsPerLine = []
        currentLine = []
        for i, word in enumerate(words):
            # print(currentLine)
            if currentLine and len(" ".join(currentLine)) + len(word) >= maxWidth:
                spaces = len(currentLine) - 1
                spacesToCover = maxWidth - len("".join(currentLine))
                if spaces > 0:
                    spaceSize = spacesToCover // spaces
                    additionalSpace = spacesToCover % spaces
                else:
                    spaceSize = spacesToCover
                    additionalSpace = 0
                line = ""
                # print(spaceSize, additionalSpace)
                for j, lineWord in enumerate(currentLine):
                    line += currentLine[j]
                    if j < len(currentLine) - 1 or j == 0:
                        line += " " * spaceSize
                    if additionalSpace > 0 and j // additionalSpace == 0:
                        line += " "
                wordsPerLine.append(line)
                currentLine = []
            currentLine.append(word)
        
        if currentLine:
            line = " ".join(currentLine)
            wordsPerLine.append(line + " " * (maxWidth - len(line)))

        return wordsPerLine
