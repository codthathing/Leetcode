class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        consecutiveCount = 0
        listConsecutiveOnes: list[int] = []

        for i, n in enumerate(nums):
            if n == 1:
                consecutiveCount += 1
                
                if (i + 1) < len(nums):
                    if nums[i + 1] == 0:
                        listConsecutiveOnes.append(consecutiveCount)
                elif (i + 1) == len(nums):
                    listConsecutiveOnes.append(consecutiveCount)
            else:
                consecutiveCount = 0

                listConsecutiveOnes.append(consecutiveCount)

        return max(listConsecutiveOnes)


nums: list[int] =[1,1,0,1,1,1]

practice = Solution()
print(practice.findMaxConsecutiveOnes(nums))