student_name = input("Enter student name: ")
python_score = float(input("Enter Python score: "))
english_score = float(input("Enter English score: "))
math_score = float(input("Enter Mathematics score: "))

average = (python_score + english_score + math_score) / 3

print("\n========================================")
print("          STUDENT RESULT")
print("========================================")
print(f"Student: {student_name}")
print(f"Python:       {python_score:>6.2f}")
print(f"English:      {english_score:>6.2f}")
print(f"Mathematics:  {math_score:>6.2f}")
print("----------------------------------------")
print(f"Average:      {average:>6.2f}")
print("========================================")