# Student Management System

records = [
 ["Aman", "Math", 88],
 ["Priya", "Physics", 91],
 ["Rahul", "Math", 76],
 ["Avishka", "English", 95],
 ["Anant", "Physics", 87],
 ["Sharanya", "Physics", 92],
 ["Mona", "Math", 71],
 ["Aakriti", "English", 86],
 ["Aayush", "English", 56],
 ["Karan", "Math", 90]
]


# 1️⃣ Add Student
def add_student(name, subject, marks):

    # prevent duplicate name + subject
    for r in records:
        if r[0] == name and r[1] == subject:
            print("Duplicate record not allowed")
            return

    records.append([name, subject, marks])
    print("Student added successfully")


# 2️⃣ Get Toppers
def get_toppers(subject):

    subject_students = [r for r in records if r[1] == subject]

    sorted_students = sorted(subject_students, key=lambda x: x[2], reverse=True)

    toppers = sorted_students[:3]
    #print(toppers)

    print("Top students in", subject)

    for t in toppers:
        print(t)


# 3️⃣ Class Average
def class_average(subject):

    marks = [m[2] for m in records if m[1] == subject]

    if len(marks) == 0:
        return 0

    avg = sum(marks) / len(marks)

    print("Class average for", subject, "=", round(avg, 2))

    return avg


# 4️⃣ Above Average Students
def above_average_students():

    all_marks = [r[2] for r in records]

    class_avg = sum(all_marks) / len(all_marks)

    students = [r[0] for r in records if r[2] > class_avg]

    print("Class average =", round(class_avg, 2))
    print("Students above average:")

    for s in students:
        print(s)


# 5️⃣ Remove Student
def remove_student(name):

    global records

    records = [r for r in records if r[0] != name]

    print("Student removed if existed")


# 6️⃣ Save Records to File
def save_records():

    file = open("students.txt", "w")

    for r in records:
        line = f"{r[0]}, {r[1]}, {r[2]}\n"
        file.write(line)

    file.close()

    print("Records saved to students.txt")


# 7️⃣ Menu Driven CLI
def menu():

    while True:

        print("\nStudent Management System")
        print("1 Add student")
        print("2 Show toppers")
        print("3 Show class average")
        print("4 Show above-average students")
        print("5 Remove student")
        print("6 Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            name = input("Enter name: ")
            subject = input("Enter subject (English, Math, Physics): ")
            marks = int(input("Enter marks: "))

            add_student(name, subject, marks)

        elif choice == "2":

            subject = input("Enter subject (English, Math, Physics): ")
            get_toppers(subject)

        elif choice == "3":

            subject = input("Enter subject (English, Math, Physics):: ")
            class_average(subject)

        elif choice == "4":

            above_average_students()

        elif choice == "5":

            name = input("Enter student name: ")
            remove_student(name)

        elif choice == "6":

            save_records()
            print("Exiting program")
            break

        else:
            print("Invalid choice")


# Run program
menu()