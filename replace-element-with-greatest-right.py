class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_so_far = -1
        
        for i in range(len(arr) - 1, -1, -1):
            current: int = arr[i]
            arr[i] = max_so_far
            if current > max_so_far:
                max_so_far: int = current

        return arr


practice = Solution()

arr: list[int] = [17,18,5,4,6,1]
print(practice.replaceElements(arr))