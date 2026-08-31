class Solution:
    def addDigits(self, num: int) -> int:
        stringNum: str = f"{num}"

        if len(stringNum) == 1:
            return int(stringNum)

        sum: int = 0
        for l in zip(stringNum):
            number = int(next(iter(l)))
            sum += number

        return self.addDigits(sum)


practice = Solution()
print(practice.addDigits(0))