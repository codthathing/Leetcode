class Solution:
  def getConcatenation(self, nums: list[int]) -> list[int]:
    ans: list[int] = []
    numsLength: int = len(nums)

    for i, n in enumerate(nums):
      ans.insert(i, n)
      ans.insert((i + numsLength), n)

    return ans

newArrayObject = Solution()
print(newArrayObject.getConcatenation([1,4,1,2]))

        