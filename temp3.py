def get_course_info():
    course_number = input("Enter course number: ")
    course_name = input("Enter course name: ")
    letter_grade = input("Enter letter grade: ")
    credit_hours = float(input("Enter credit hours: "))
    
    return course_number, course_name, letter_grade, credit_hours

def calculate_quality_points(letter_grade):
    grade_points = {
        'A': 4.00, 'A-': 3.67, 'B+': 3.33,
        'B': 3.00, 'B-': 2.67, 'C+': 2.33,
        'C': 2.00, 'C-': 1.67, 'D+': 1.33,
        'D': 1.00, 'F': 0.00
    }

    return grade_points.get(letter_grade, 0.00)

def calculate_semester_gpa(total_quality_points, total_credit_hours):
    if total_credit_hours == 0:
        return 0.00
    return total_quality_points / total_credit_hours

def main():
    total_classes = int(input("Enter the total number of classes: "))
    
    total_quality_points = 0
    total_credit_hours = 0
    
    for _ in range(total_classes):
        print("\nEnter information for class #", _ + 1)
        course_number, course_name, letter_grade, credit_hours = get_course_info()
        
        quality_points = calculate_quality_points(letter_grade)
        total_quality_points += quality_points * credit_hours
        total_credit_hours += credit_hours

    semester_gpa = calculate_semester_gpa(total_quality_points, total_credit_hours)

    if semester_gpa < 0.00 or semester_gpa > 4.00:
        print("Error: GPA out of range.")
    else:
        print(f"\nSemester GPA: {semester_gpa:.2f}")
        print("Letter Grade:", end=" ")

        if semester_gpa >= 3.67:
            print("A")
        elif semester_gpa >= 3.33:
            print("A-")
        elif semester_gpa >= 3.00:
            print("B+")
        elif semester_gpa >= 2.67:
            print("B")
        elif semester_gpa >= 2.33:
            print("B-")
        elif semester_gpa >= 2.00:
            print("C+")
        elif semester_gpa >= 1.67:
            print("C")
        elif semester_gpa >= 1.33:
            print("C-")
        elif semester_gpa >= 1.00:
            print("D+")
        elif semester_gpa >= 0.00:
            print("D")
        else:
            print("F")

if __name__ == "__main__":
    main()
