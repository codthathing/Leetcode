class Solution:
    def __init__(self) -> None:
        self.numbers: set[int] = set()

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        if n in self.numbers:
            return False

        self.numbers.add(n)

        sum: int = 0
        for number in str(n):
            sum += int(number)**2

        return self.isHappy(sum)


practice = Solution()
print(practice.isHappy(4))