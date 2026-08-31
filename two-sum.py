class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        listNum: dict[int, list[int]] = {}

        for i, num in enumerate(nums):
            if num in listNum:
                listNum[num].append(i)

                return listNum[num]
            else:
                listNum[target - num] = [i]

        return []

practice = Solution()
print(practice.twoSum([-3,4,3,90], 0))