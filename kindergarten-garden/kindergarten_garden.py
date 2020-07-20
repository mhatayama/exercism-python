class Garden:
    DEFAULT_STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    PLANTS = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"}

    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.diagrams = diagram.split()
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student)
        abbr_plants = [self.diagrams[0][index * 2], self.diagrams[0][index * 2 + 1],
                self.diagrams[1][index * 2], self.diagrams[1][index * 2 + 1]]
        return [self.PLANTS[c] for c in abbr_plants]
