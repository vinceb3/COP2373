import csv

def main():
    # Very simple progression from writing to reading, but can be quit
    # from the write_grades() function by typing a non-digit
    write_grades()
    read_grades()

# The write_grades() function writes values to grades.csv.
def write_grades():
    # Uses a try-except block as a safe way to exit the program (such as
    # if there's already a record that the teacher doesn't want to delete)
    try:
        # Asks the teacher how many students' scores to record
        num_students = int(input("How many students would you like to record? (type "
                                 "anything but a digit to quit): "))
    except ValueError:
        print("Program terminated.")

    with open("grades.csv", "w", newline="") as gradesCSV:
        writer = csv.writer(gradesCSV)

        # Creates the header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Asks the user for student info, then writes it to the file
        for x in range(num_students):
            num_student = x + 1
            first_name = input(f"Student {num_student}'s first name: ")
            last_name = input(f"Student {num_student}'s last name: ")
            exam1 = int(input(f"Student {num_student}'s first exam score: "))
            exam2 = int(input(f"Student {num_student}'s second exam score: "))
            exam3 = int(input(f"Student {num_student}'s third exam score: "))
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

# The read_grades() function prints grades.csv in table format.
def read_grades():
    with open("grades.csv", "r") as gradesCSV:
        reader = csv.reader(gradesCSV)
        for row in reader:
            # Formats the table to account for expected value sizes
            print("{:<13} {:<13} {:<7} {:<7} {:<7}".format(*row))


if __name__ == "__main__":
    main()