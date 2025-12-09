class Solution(object):
    def countStudents(self, students, sandwiches):
        studentsLeft = False

        while not studentsLeft:
            lengthOfSandwich = len(sandwiches)

            for j in range(len(students)):
                if students[0] == sandwiches[0]:
                    sandwiches.pop(0)
                    students.pop(0)
                else:
                    firstStudent = students[0]
                    for i in range(len(students) - 1):
                        students[i] = students[i + 1]

                    students[len(students) - 1] = firstStudent

            if not students or len(sandwiches) == lengthOfSandwich:
                studentsLeft = True

        return len(students)
    

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]

practice = Solution()
print(practice.countStudents(students, sandwiches))