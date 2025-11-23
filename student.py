from datetime import datetime

class Person:
    def __init__(self, student_id, name, email, phone=None):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.role = "Person"

class Student(Person):
    def __init__(self, student_id, name, email, phone=None):
        super().__init__(student_id, name, email, phone)
        self.role = "Student"
        self.courses = []
        self.grades = {}
        self.attendance = {}
        self.last_login = datetime.now()

    def register_course(self, course):
        if course.code not in [c.code for c in self.courses]:
            self.courses.append(course)
            print(f"{self.name} registered for {course.title}")

    # --- New smaller methods ---

    def calculate_gpa(self):
        grade_points = {"A":4, "B":3, "C":2, "D":1, "E":0}
        total = sum(grade_points.get(g, 0) for g in self.grades.values())
        return round(total / len(self.grades), 2) if self.grades else 0

    def calculate_attendance(self):
        percentages = []
        for course, records in self.attendance.items():
            if records:
                attended = len([r for r in records if r])
                percentages.append((attended / len(records)) * 100)
        return sum(percentages) / len(percentages) if percentages else 0

    def calculate_performance(self):
        gpa = self.calculate_gpa()
        attendance = self.calculate_attendance()
        print(f"GPA: {gpa}, Attendance: {attendance:.1f}%")

        if gpa >= 3.5 and attendance >= 90:
            print("Excellent performance!")
        elif gpa < 2.0 or attendance < 60:
            print("Warning: Poor performance")
        return gpa
