class Class(object):

    MAX_NUM_OF_STUDENTS = 5

    def __init__(self, class_number=-1, subject="", teacher=None):
        self.students = []
        self.class_number = class_number
        self.subject = subject
        self.teacher = teacher
        self.student_in_class_now = []

    @property
    def has_place(self):
        return len(self.students) < self.MAX_NUM_OF_STUDENTS

    def add_student(self, student):
        if not self.has_place:
            raise SystemError("No place left on class {}".format(self.class_number))
        self.students.append(student)

    def can_enter_class(self, student):
        return student in self.students

    def can_exit_class(self, student):
        return student in self.student_in_class_now

    def student_enter(self, student):
        self.student_in_class_now.append(student)

    def student_exit(self, student):
        self.student_in_class_now.remove(student)
