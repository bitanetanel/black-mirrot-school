from Class import Class
from Teacher import Teacher
from Student import Student
from black_mirror.events import EventsLogger, EnterClass, ExitClass


class School(object):

    NUM_OF_CLASSES = 8

    def __init__(self):
        self.classes = []
        self.teachers = []
        self.students = []
        self.init_classes()

    def init_classes(self):
        """
        Create the max num of classes.
        """
        for i in xrange(self.NUM_OF_CLASSES):
            self.classes.append(Class(i))

    def add_teacher(self, name, phone, class_number):
        if self.get_class(class_number):
            teacher = Teacher(name, phone, class_number)
            self.teachers.append(teacher)
            self.get_class(class_number).teacher = teacher

    def add_student(self, name, phone, age):
        """
        Add a new student, return the id of it after creation.

        :return: The id of the user that was created.
        """
        student = Student(name, phone, age, school=self)
        self.students.append(student)
        return self.students.index(student)

    def get_class(self, class_number):
        """
        :return: The class in the given number
        :rtype: Class
        """
        if class_number > len(self.classes):
            raise ValueError("There is not class with number {}".format(class_number))
        return self.classes[class_number]

    def get_student(self, student_id):
        """
        :return: The student with the given id.
        :rtype: Student
        """
        if student_id > len(self.students):
            raise ValueError("There is not student with id {}".format(student_id))
        return self.students[student_id]

    def enter_class(self, student_id, class_number):
        student = self.get_student(student_id)
        klass = self.get_class(class_number)
        if student.can_enter_class(class_number) and klass.can_enter_class(student):
            klass.student_enter(student)
            EventsLogger.log(EnterClass(student, class_number))
        else:
            raise SystemError("{} can not enter class number {}".format(student_id, class_number))

    def exit_class(self, student_id, class_number):
        student = self.get_student(student_id)
        klass = self.get_class(class_number)
        if klass.can_exit_class(student):
            klass.student_exit(student)
            EventsLogger.log(ExitClass(student, class_number))
        else:
            raise SystemError("{} can not exit class number {}".format(student_id, class_number))