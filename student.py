print("Welcome to the Student Data Organizer!")

my_std_list = []

while True:
    print("\nSelect an option:")
    print("1. Add student")
    print("2. Display all students")
    print("3. Update student information")
    print("4. Delete student")
    print("5. Display subjects offered")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nEnter Student Details:")
        sid = input("Student ID: ")
        sname = input("Name: ")
        sage = int(input("Age: "))
        sGrade = input("Grade: ")
        sDOB = input("Date of Birth: ")
        sSub = input("Subjects (comma-separated): ").split(',')

        student = {
            "id": sid,
            "name": sname,
            "age": sage,
            "grade": sGrade,
            "dob": sDOB,
            "subjects": [subject.strip() for subject in sSub]
        }

        my_std_list.append(student)
        print("\nStudent added successfully!")

    elif choice == 2:
        print("\n--- Displaying All Students ---")
        if not my_std_list:
            print("No students found.")
        else:
            for student in my_std_list:
                print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}")

    elif choice == 3:
        update_id = input("Enter Student ID to update: ")
        found = False
        for student in my_std_list:
            if student['id'] == update_id:
                found = True
                print("Leave a field empty to keep current value.")

                new_name = input(f"New Name (current: {student['name']}): ") or student['name']
                new_age_input = input(f"New Age (current: {student['age']}): ")
                new_age = int(new_age_input) if new_age_input else student['age']
                new_grade = input(f"New Grade (current: {student['grade']}): ") or student['grade']
                new_dob = input(f"New DOB (current: {student['dob']}): ") or student['dob']
                new_subjects_input = input(f"New Subjects (comma-separated, current: {', '.join(student['subjects'])}): ")
                new_subjects = [s.strip() for s in new_subjects_input.split(',')] if new_subjects_input else student['subjects']

                student.update({
                    "name": new_name,
                    "age": new_age,
                    "grade": new_grade,
                    "dob": new_dob,
                    "subjects": new_subjects
                })

                print("Student data updated successfully!")
                break
        if not found:
            print("Student not found.")

    elif choice == 4:
        delete_id = input("Enter Student ID to delete: ")
        for student in my_std_list:
            if student['id'] == delete_id:
                my_std_list.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    elif choice == 5:
        print("\n--- Displaying All Subjects Offered ---")
        all_subjects = set()
        for student in my_std_list:
            all_subjects.update(student['subjects'])
        print(", ".join(all_subjects) if all_subjects else "No subjects found.")

    elif choice == 6:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
