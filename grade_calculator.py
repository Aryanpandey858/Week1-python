"""Student Grade Calculator: take marks, calculate average, assign grade."""


def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    elif avg >= 40:
        return "E"
    else:
        return "F (Fail)"


def main():
    print("=== Student Grade Calculator ===")
    name = input("Enter student name: ").strip()

    try:
        n = int(input("How many subjects? "))
        if n <= 0:
            print("Number of subjects must be at least 1.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    marks = []
    for i in range(1, n + 1):
        while True:
            try:
                m = float(input(f"Enter marks for subject {i} (0-100): "))
                if 0 <= m <= 100:
                    marks.append(m)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    avg = calculate_average(marks)
    print("\n--- Result ---")
    print(f"Student : {name}")
    print(f"Total   : {sum(marks):.2f} / {n * 100}")
    print(f"Average : {avg:.2f}")
    print(f"Grade   : {assign_grade(avg)}")


if __name__ == "__main__":
    main()