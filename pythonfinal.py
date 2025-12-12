
def add_student(gradebook):
    name = input("Enter student name: ").strip()

    try:
        num_grades = int(input("How many grades to enter? "))
    except ValueError:
        print("Please type a number.")
        return

    grades = []
    for i in range(num_grades):
        while True:
            try:
                grade = float(input(f"Enter grade #{i+1}: "))
                grades.append(grade)
                break
            except ValueError:
                print("Please type a valid number.")

    gradebook[name] = grades
    print(f"{name} added.\n")



def show_gradebook(gradebook):
    if not gradebook:
        print("No students yet.\n")
        return

    print("\n------ Gradebook ------")
    for name, grades in gradebook.items():
        print(f"{name}: {grades}")
    print()



def show_averages(gradebook):
    if not gradebook:
        print("No students yet.\n")
        return

    print("\n------ Student Averages ------")
    for name, grades in gradebook.items():
        if grades:
            avg = sum(grades) / len(grades)
            print(f"{name}: {avg:.2f}")
        else:
            print(f"{name}: No grades entered.")
    print()


def main():
    gradebook = {} 

    while True:
        print("1. Add Student")
        print("2. View Gradebook")
        print("3. View Averages")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(gradebook)
        elif choice == "2":
            show_gradebook(gradebook)
        elif choice == "3":
            show_averages(gradebook)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

main()
