class Solution:
    def calPoints(self, operations: list[str]) -> int:
        records: list[int] = []

        for n in operations:
            match (n):
                case "+":
                    records.append(records[-1] + records[-2])
                case "D":
                    records.append(2 * records[-1])
                case "C":
                    records.pop()
                case _:
                    records.append(int(n))

        return sum(records)


practice = Solution()
print(practice.calPoints(["1","2","+","C","5","D"]))