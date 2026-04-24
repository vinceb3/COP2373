import numpy as np
import csv

# The assemble_data() function creates an array composed of data from the
# grades.csv file, prints a test of the data's structure, and returns the
# array.
def assemble_data():
    # Initialize a list for the CSV data
    grades = []

    with open("grades.csv", "r") as file:
        reader = csv.reader(file)

        # Skips the header
        next(reader)

        # Add the scores of every student to the list
        for row in reader:
            grades.append(row[2:])

    # Create an array from the list using the float data type
    grades_array = np.array(grades, dtype=float)

    # Test of data structure
    print("First few rows: ")
    print(grades_array[:3])
    print()

    return grades_array

def grades_analysis(grades):
    # Analyzes each exam for mean, median, standard deviation, min, and max
    means = np.mean(grades, axis=0)
    medians = np.median(grades, axis=0)
    stds = np.std(grades, axis=0)
    mins = np.min(grades, axis=0)
    maxes = np.max(grades, axis=0)

    # Print results, using .join and formatting to make everything look pretty
    print("--- Analysis of exams 1, 2, and 3 ---")
    print()
    print(f"Means: {', '.join(f'{n:.1f}%' for n in means)}")
    print(f"Medians: {', '.join(f'{n:.1f}%' for n in medians)}")
    print(f"Standard Deviations: {', '.join(f'{n:.1f}' for n in stds)}")
    print(f"Lowest scores: {', '.join(f'{n:.1f}%' for n in mins)}")
    print(f"Highest scores: {', '.join(f'{n:.1f}%' for n in maxes)}")
    print()
    print(f"Overall mean: {np.mean(grades):.1f}%")
    print(f"Overall median: {np.median(grades):.1f}%")
    print(f"Overall standard deviation: {np.std(grades):.1f}")
    print(f"Lowest score: {np.min(grades):.1f}%")
    print(f"Highest Score: {np.max(grades):.1f}%")
    print()

   # Creates variables for numbers of students and exams
    students = len(grades)
    exams = len(grades[0])

    # Sets up an accumulator for the pass percentage
    overall_passes = 0

    # Calculates number of students passed for each exam, and prints results
    for exam in range(exams):
        passed_exam, failed_exam = 0, 0
        for row in grades:
            if row[exam] >= 60:
                passed_exam += 1
                overall_passes += 1
            else:
                failed_exam += 1
        print(f"Exam {exam +1}: {passed_exam} students passed, {failed_exam} students failed.")

    # Calculates and prints pass percentage
    pass_percentage = overall_passes / (students * exams)
    print(f"Pass percentage: {pass_percentage:.2%}")

def main():
    grades_analysis(assemble_data())

if __name__ == "__main__":
    main()

