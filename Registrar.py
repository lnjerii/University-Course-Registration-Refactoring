class ReportGenerator:
    def course_report(self, courses):
        for c in courses:
            c.display_details()

    def lecturer_report(self, lecturers):
        for l in lecturers:
            l.print_summary()

    def student_report(self, students):
        for s in students:
            s.calculate_performance()


class Registrar:
    def __init__(self):
        self.students = []
        self.courses = []
        self.lecturers = []
        self.reporter = ReportGenerator()

    def add_student(self, s): self.students.append(s)
    def add_course(self, c): self.courses.append(c)
    def add_lecturer(self, l): self.lecturers.append(l)

    def full_report(self):
        print("=== Full University Report ===")
        self.reporter.course_report(self.courses)
        self.reporter.lecturer_report(self.lecturers)
        self.reporter.student_report(self.students)
