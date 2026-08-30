class Solution:
    def fizzBuzz(self, n: int) -> list[int | str]:
        answer: list[int | str] = []

        for i in range(n):
            intByThree: bool = (i + 1)%3 == 0
            intByFive: bool = (i + 1)%5 == 0

            if intByThree and intByFive:
                answer.insert(i, "FizzBuzz")
            elif intByThree:
                answer.insert(i, "Fizz")
            elif intByFive:
                answer.insert(i, "Buzz")
            else:
                answer.insert(i, i + 1)
        return answer

practice = Solution()
print(practice.fizzBuzz(15))