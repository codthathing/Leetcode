class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        i: int = len(arr)
        maxElement: int = 0

        while i > 0:
            currentElement: int = arr[i-1]

            arr[i-1] = -1 if i == len(arr) else maxElement
            maxElement: int = max(currentElement, maxElement)

            i-=1

        return arr


practice = Solution()

arr: list[int] = [17,18,5,4,6,1]
print(practice.replaceElements(arr))