class Solution:
    def __init__(self) -> None:
        self.stepsDicts: dict[int, int] = {}

    def climbStairs(self, n: int) -> int:
        possibleStepsTaken = 0

        if n in self.stepsDicts:
            return self.stepsDicts[n]

        if n == 1:
            possibleStepsTaken += 1
        elif n == 2:
            possibleStepsTaken += 2
        else:
            result: int = self.climbStairs(n - 2) + self.climbStairs(n - 1)
            self.stepsDicts[n] = result

            return result
        
        return possibleStepsTaken
        

practice = Solution()
print(practice.climbStairs(44))
