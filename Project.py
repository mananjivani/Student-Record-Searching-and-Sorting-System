


students = []


def add_student():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["roll"] == roll:
            print("Roll number already exists!")
            return

    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    marks = float(input("Enter Marks: "))

    students.append({
        "roll": roll,
        "name": name,
        "department": department,
        "marks": marks
    })

    print("Student record added successfully!")


def display_students(records=None):
    if records is None:
        records = students

    if not records:
        print("No student records found.")
        return

    print("\n{:<10} {:<20} {:<15} {:<10}".format(
        "Roll No.", "Name", "Department", "Marks"
    ))
    print("-" * 55)

    for s in records:
        print("{:<10} {:<20} {:<15} {:<10}".format(
            s["roll"], s["name"],
            s["department"], s["marks"]
        ))


# Linear Search: O(n)
def linear_search(roll):
    for student in students:
        if student["roll"] == roll:
            return student
    return None


# Binary Search: O(log n)
# Records are sorted by roll number first.
def binary_search(roll):
    records = merge_sort(students.copy(), "roll")
    low = 0
    high = len(records) - 1

    while low <= high:
        mid = (low + high) // 2

        if records[mid]["roll"] == roll:
            return records[mid]
        elif records[mid]["roll"] < roll:
            low = mid + 1
        else:
            high = mid - 1

    return None


# Bubble Sort: O(n^2)
def bubble_sort(records, key):
    result = records.copy()
    n = len(result)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if result[j][key] > result[j + 1][key]:
                result[j], result[j + 1] = (
                    result[j + 1], result[j]
                )
                swapped = True

        if not swapped:
            break

    return result


# Merge Sort: O(n log n)
def merge_sort(records, key):
    if len(records) <= 1:
        return records.copy()

    mid = len(records) // 2
    left = merge_sort(records[:mid], key)
    right = merge_sort(records[mid:], key)

    return merge(left, right, key)


def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def search_student():
    try:
        roll = int(input("Enter Roll Number to Search: "))
    except ValueError:
        print("Please enter a valid roll number.")
        return

    print("1. Linear Search")
    print("2. Binary Search")
    choice = input("Choose Search Algorithm: ")

    if choice == "1":
        result = linear_search(roll)
    elif choice == "2":
        result = binary_search(roll)
    else:
        print("Invalid choice!")
        return

    if result:
        print("\nStudent Found:")
        display_students([result])
    else:
        print("Student record not found.")


def sort_students():
    if not students:
        print("No records to sort.")
        return

    print("Sort By:")
    print("1. Roll Number")
    print("2. Name")
    print("3. Marks")
    key_choice = input("Enter choice: ")

    keys = {
        "1": "roll",
        "2": "name",
        "3": "marks"
    }

    if key_choice not in keys:
        print("Invalid choice!")
        return

    key = keys[key_choice]

    print("1. Bubble Sort")
    print("2. Merge Sort")
    algorithm = input("Choose Sorting Algorithm: ")

    if algorithm == "1":
        sorted_records = bubble_sort(students, key)
    elif algorithm == "2":
        sorted_records = merge_sort(students, key)
    else:
        print("Invalid choice!")
        return

    print("\nSorted Student Records:")
    display_students(sorted_records)


def main():
    while True:
        print("\n===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Sort Student Records")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            sort_students()
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
