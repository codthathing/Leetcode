class Solution:
  def getConcatenation(self, nums: list[int]) -> list[int]:
    length: int = len(nums)
    ans: list[int] = [0] * (2 * length)

    for i in range(length):
      ans[i] = nums[i]
      ans[i + length] = nums[i]
        
    return ans

newArrayObject = Solution()
print(newArrayObject.getConcatenation([1,4,1,2]))

        