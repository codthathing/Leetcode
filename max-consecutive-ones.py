class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        current_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_count: int = current_count + 1
                if current_count > max_count:
                    max_count: int = current_count
            else:
                current_count = 0
        return max_count


nums: list[int] =[1,1,0,1,1,1]

practice = Solution()
print(practice.findMaxConsecutiveOnes(nums))