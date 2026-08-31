class Solution:
    def firstUniqChar(self, s: str) -> int:
        nonRepeating: dict[str, int] = {}

        for c in s:
            if c in nonRepeating:
                nonRepeating[c] += 1
            else:
                nonRepeating[c] = 1

        for key, value in nonRepeating.items():
            if value == 1:
                return s.index(key)

        return -1

practice = Solution()
print(practice.firstUniqChar("aabb"))