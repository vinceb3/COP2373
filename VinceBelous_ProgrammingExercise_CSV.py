import csv

def main():
    write_grades()
    read_grades()

def write_grades():
    num_students = int(input("How many students would you like to record? "))

    with open("grades.csv", "w", newline="") as gradesCSV:
        writer = csv.writer(gradesCSV)

        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        for x in range(num_students):
            num_student = x + 1
            first_name = input(f"Student {num_student}'s first name: ")
            last_name = input(f"Student {num_student}'s last name: ")
            exam1 = int(input(f"Student {num_student}'s first exam score: "))
            exam2 = int(input(f"Student {num_student}'s second exam score: "))
            exam3 = int(input(f"Student {num_student}'s third exam score: "))
            writer.writerow([first_name, last_name, exam1, exam2, exam3])



def read_grades():
    with open("grades.csv", "r") as gradesCSV:
        reader = csv.reader(gradesCSV)
        for row in reader:
            print("{:<13} {:<13} {:<7} {:<7} {:<7}".format(*row))


if __name__ == "__main__":
    main()