# students = []

# with open("students.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()

# for line in lines:
#     data = line.strip().split(",")

#     student = {
#         "name": data[0],
#         "score": int(data[1])
#     }

#     students.append(student)

# print(students)



# def save_students(students, filename):
#     with open(filename, "w", encoding="utf-8") as file:
#         for student in students:
#             line = f"{student['name']},{student['score']}\n"
#             file.write(line)

# save_students(students, "test.txt")

import os
d = os.getcwd()
print(os.getcwd())


if os.path.exists("ranking.txt"):
    print("랭킹 파일이 있습니다.")

else:
    print("랭킹 파일이 없습니다.")