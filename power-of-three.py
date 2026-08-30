class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True

        if n == 0:
            return False

        if n % 3 == 0:
            return self.isPowerOfThree(int(n / 3))
        else:
            return False

practice = Solution()
print(practice.isPowerOfThree(1))
  