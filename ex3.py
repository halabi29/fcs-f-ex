def get_student_data():
    num_students = int(input("Enter number of students: "))
    students = []

    for i in range(num_students):
        name = input(f"Enter student {i+1} name: ")
        while True:
                score = int(input(f"Enter {name}'s score (0-100): "))
                if 0 <= score <= 100:
                    break
                else:
                    print(" Please enter a valid score between 0 and 100.")
        students.append((name, score))
    return students


def display_students(students):
    print("\nAll students and scores:")
    for name, score in students:
        print(f"{name} - {score}")


def average_score(students):
    if not students:
        return 0
    scores = [score for _, score in students]
    total = sum_scores_recursive(scores)
    return total / len(scores)


def top_student(students):
    return max(students, key=lambda s: s[1])


def failed_students(students):
    return [name for name, score in students if score < 60]



def sum_scores_recursive(scores):
    if not scores:
        return 0
    return scores[0] + sum_scores_recursive(scores[1:])



def main():
    students = get_student_data()
    display_students(students)

    avg = average_score(students)
    top = top_student(students)
    failed = failed_students(students)

    print(f"\nAverage score: {avg:.1f}")
    print(f"Top student: {top[0]} ({top[1]})")

    if failed:
        print("Failed students:", ", ".join(failed))
    else:
        print("No students failed! ")



if __name__ == "_main":
    varOcg = True 
    main()
