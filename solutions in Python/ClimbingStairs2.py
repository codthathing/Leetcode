class Solution(object):
    def __init__(self):
        self.stepsDicts = {}

    def cost(self, i, j, costs):
        return costs[j - 1] + ((j - i) ** 2)

    def climbStairs(self, n, costs, currentStep=0):
        if currentStep in self.stepsDicts:
            return self.stepsDicts[currentStep]

        if currentStep == n:
            return 0
        elif currentStep == n - 1:
            return self.cost(currentStep, n, costs)
        elif currentStep == n - 2:
            return min(
                self.cost(currentStep, n - 1, costs) + self.climbStairs(n, costs, n - 1),
                self.cost(currentStep, n, costs),
            )
        elif currentStep == n - 3:
            return min(
                self.cost(currentStep, n - 1, costs) + self.climbStairs(n, costs, n - 1),
                self.cost(currentStep, n - 2, costs) + self.climbStairs(n, costs, n - 2),
                self.cost(currentStep, n, costs),
            )
        else:
            stepOne = self.cost(currentStep, currentStep + 1, costs) + self.climbStairs(n, costs, currentStep + 1)
            stepTwo = self.cost(currentStep, currentStep + 2, costs) + self.climbStairs(n, costs, currentStep + 2)
            stepThree = self.cost(currentStep, currentStep + 3, costs) + self.climbStairs(n, costs, currentStep + 3)

            result = min(stepOne, stepTwo, stepThree)

            self.stepsDicts[currentStep] = result

            return min(stepOne, stepTwo, stepThree)


practice = Solution()
print(practice.climbStairs(5, [9,4,4,5,6]))
