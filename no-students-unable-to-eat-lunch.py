class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        studentsLeft = False

        while not studentsLeft:
            lengthOfSandwich: int = len(sandwiches)

            for _ in range(len(students)):
                if students[0] == sandwiches[0]:
                    sandwiches.pop(0)
                    students.pop(0)
                else:
                    firstStudent: int = students[0]
                    for i in range(len(students) - 1):
                        students[i] = students[i + 1]

                    students[len(students) - 1] = firstStudent

            if not students or len(sandwiches) == lengthOfSandwich:
                studentsLeft = True

        return len(students)
    

students: list[int] = [1,1,1,0,0,1]
sandwiches: list[int] = [1,0,0,0,1,1]

practice = Solution()
print(practice.countStudents(students, sandwiches))