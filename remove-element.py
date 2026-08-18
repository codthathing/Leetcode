class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        expectedNums: int = 0

        for num in nums:
            if num != val:
                expectedNums += 1

        return expectedNums


practice = Solution()

nums: list[int] = [3,2,2,3]
print(practice.removeElement(nums, 3))