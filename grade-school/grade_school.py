class School:
    def __init__(self):
        self.students_by_grade = {}

    def add_student(self, name, grade):
        if not grade in self.students_by_grade:
            self.students_by_grade[grade] = [name]
        else:
            self.students_by_grade[grade].append(name)

    def roster(self):
        sorted_grades = sorted(self.students_by_grade.keys())
        students_sorted_by_grade = [self.grade(grade) for grade in sorted_grades]
        return [student for students in students_sorted_by_grade for student in students]

    def grade(self, grade_number):
        if not grade_number in self.students_by_grade:
            return []
        return sorted(self.students_by_grade[grade_number])
