from Registrar import Registrar, Course, Lecturer, Student


def main():
    reg = Registrar()

    c1 = Course("CS101", "Intro to Programming", 3)
    c2 = Course("CS201", "Data Structures", 4)

    l1 = Lecturer("L001", "Dr. Smith", "smith@uni.com", "CS")
    reg.add_lecturer(l1)

    s1 = Student("S001", "Alice", "alice@uni.com")
    s2 = Student("S002", "Bob", "bob@uni.com")
    reg.add_student(s1)
    reg.add_student(s2)

    # Assign courses
    l1.assign_course(c1)
    c1.enroll_student(s1)
    c1.enroll_student(s2)

    # Grades & Attendance
    l1.submit_grades([s1, s2], "CS101", "A")
    s1.attendance["CS101"] = [True, True, False, True]
    s2.attendance["CS101"] = [True, False, True, False]

    reg.add_course(c1)
    reg.add_course(c2)

    reg.full_report()
