# import numpy as np

# # -----------------------------------
# # 1. Student Data
# # -----------------------------------

# students = np.array([
#     ["Ayush", 85, 90, 78],
#     ["Rahul", 72, 65, 80],
#     ["Priya", 92, 88, 95],
#     ["Neha", 60, 70, 68],
#     ["Aman", 78, 82, 75]
# ])

# names = students[:, 0]

# marks = students[:, 1:].astype(int)

# subjects = np.array(["Math", "Science", "English"])


# # -----------------------------------
# # 2. Basic Information
# # -----------------------------------

# print("===== STUDENT PERFORMANCE ANALYZER =====\n")

# print("Number of Students:", marks.shape[0])
# print("Number of Subjects:", marks.shape[1])


# # -----------------------------------
# # 3. Student-wise Analysis
# # -----------------------------------

# total_marks = np.sum(marks, axis=1)
# average_marks = np.mean(marks, axis=1)

# print("\n===== STUDENT PERFORMANCE =====")

# for i in range(len(names)):
#     print(
#         f"{names[i]} -> "
#         f"Total: {total_marks[i]}, "
#         f"Average: {average_marks[i]:.2f}"
#     )


# # -----------------------------------
# # 4. Subject-wise Analysis
# # -----------------------------------

# subject_average = np.mean(marks, axis=0)
# subject_highest = np.max(marks, axis=0)
# subject_lowest = np.min(marks, axis=0)

# print("\n===== SUBJECT PERFORMANCE =====")

# for i in range(len(subjects)):
#     print(
#         f"{subjects[i]} -> "
#         f"Average: {subject_average[i]:.2f}, "
#         f"Highest: {subject_highest[i]}, "
#         f"Lowest: {subject_lowest[i]}"
#     )


# # -----------------------------------
# # 5. Overall Statistics
# # -----------------------------------

# overall_average = np.mean(marks)
# overall_highest = np.max(marks)
# overall_lowest = np.min(marks)
# overall_std = np.std(marks)

# print("\n===== OVERALL STATISTICS =====")

# print("Overall Average:", round(overall_average, 2))
# print("Highest Mark:", overall_highest)
# print("Lowest Mark:", overall_lowest)
# print("Standard Deviation:", round(overall_std, 2))


# # -----------------------------------
# # 6. Pass / Fail Analysis
# # -----------------------------------

# passing_marks = 40

# passed = np.all(marks >= passing_marks, axis=1)

# print("\n===== PASS / FAIL =====")

# for i in range(len(names)):
#     if passed[i]:
#         print(names[i], "-> PASS")
#     else:
#         print(names[i], "-> FAIL")


# # -----------------------------------
# # 7. Top Performing Student
# # -----------------------------------

# top_student_index = np.argmax(total_marks)

# print("\n===== TOP PERFORMER =====")

# print(
#     "Top Student:",
#     names[top_student_index]
# )

# print(
#     "Total Marks:",
#     total_marks[top_student_index]
# )

# print(
#     "Average:",
#     round(average_marks[top_student_index], 2)
# )