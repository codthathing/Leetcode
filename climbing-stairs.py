class Solution(object):
    def __init__(self):
        self.stepsDicts = {}

    def climbStairs(self, n):
        possibleStepsTaken = 0

        if n in self.stepsDicts:
            return self.stepsDicts[n]

        if n == 1:
            possibleStepsTaken += 1
        elif n == 2:
            possibleStepsTaken += 2
        else:
            result = self.climbStairs(n - 2) + self.climbStairs(n - 1)
            self.stepsDicts[n] = result

            return result
        
        return possibleStepsTaken
        

practice = Solution()
print(practice.climbStairs(44))
