grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(len(grades))
grades0 = (sum(grades[0]) / len(grades[0]))
print(grades0)
grades1 = (sum(grades[1]) / len(grades[1]))
print(grades1)
grades2 = (sum(grades[2]) / len(grades[2]))
print(grades2)
grades3 = (sum(grades[3]) / len(grades[3]))
print(grades3)
grades4 = (sum(grades[4]) / len(grades[4]))
print(grades4)
grades = [grades0, grades1, grades2, grades3, grades4]
print(grades)
average_grade = grades
Students_by_alphabet = sorted(students)
print(Students_by_alphabet)
average_student_score = dict(zip(Students_by_alphabet, average_grade))
print(average_student_score)