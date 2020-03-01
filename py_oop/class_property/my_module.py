class Student:
    total_students = 0

    def __init__(self, name, sem):
        self.name = name
        self.sem = sem
        self.total_marks = 0
        Student.total_students += 1

    def add_marks(self, marks):
        self.marks = marks
        self.set_total_marks()

    def set_total_marks(self):
        self.total_marks += self.marks

    @classmethod
    def student(cls):
        return cls
    
    @classmethod
    def get_total_stds(cls):
        return cls.total_students

    def __str__(self):
        return 'Name: {}, Semester: {}, ' \
               'Total Marks: {}' \
            .format(self.name, self.sem, 
            self.total_marks)
    
    
