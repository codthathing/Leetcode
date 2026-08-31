class Solution:
    def romanToInt(self, s: str) -> int:
        intMap: dict[str, int] = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        firstPointer: int = 0
        secondPointer: int = 1

        sum: int = 0
        while (firstPointer < len(s) and secondPointer < len(s)) or firstPointer < len(s):
            if firstPointer < len(s) and secondPointer < len(s):
                if (s[firstPointer] == 'I' and (s[secondPointer] == 'V' or s[secondPointer] == 'X')) or (s[firstPointer] == 'X' and (s[secondPointer] == 'L' or s[secondPointer] == 'C')) or (s[firstPointer] == 'C' and (s[secondPointer] == 'D' or s[secondPointer] == 'M')):
                    sum += (intMap[s[secondPointer]] - intMap[s[firstPointer]])
                    firstPointer = secondPointer + 1 
                    secondPointer += 2
                else:
                    sum += intMap[s[firstPointer]]
                    firstPointer += 1 
                    secondPointer += 1

            else:
                sum += intMap[s[firstPointer]]
                firstPointer += 1

        return sum

practice = Solution()
print(practice.romanToInt("LVIII"))