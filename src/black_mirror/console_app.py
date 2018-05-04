from black_mirror.events import EventsLogger, EventTypes
from datetime import datetime, timedelta
from black_mirror.constants import DAY_HOURS

class ConsoleApp(object):
    def __init__(self, school):
        self.school = school

    def print_menu(self):
        print "Your options are:"
        print " 1) Add a student"
        print " 2) Add a teacher"
        print " 3) Enter class"
        print " 4) Exit class"
        print " 5) Eat"
        print " 6) Talk"
        print " 7) Get students"
        print " 8) Get Teachers"
        print " 9) Who ate in last 60 minutes?"
        print " 10) Presence list"
        print " 0) Exit"

    def run(self):
        self.print_menu()
        option = input("Please select option: ")

        while option:
            try:
                self.run_option(option)
            except Exception, e:
                print "Got an error: {}".format(e.message)
                print "Please try again."
            self.print_menu()
            option = input("Please select option: ")

    def add_user(self):
        print "Adding a user"
        name = raw_input("Name: ")
        phone = raw_input("Phone: ")
        age = raw_input("Age: ")
        student_id = self.school.add_student(name, phone, age)
        for i in xrange(DAY_HOURS):
            try:
                class_number = input("Select class for hour {}: ".format(i))
                self.school.get_student(student_id).set_class(class_number, i)
            except Exception, e:
                print "Got an error: {}".format(e.message)
                print "Please try again."

    def run_option(self, option):
        if option == 1:
            self.add_user()
        if option == 2:
            print "Adding a teacher"
            name = raw_input("Name: ")
            phone = raw_input("Phone: ")
            class_number = input("Class number: ")
            self.school.add_teacher(name, phone, class_number)
        if option == 3:
            print "Enter a class"
            student_id = input("Student id")
            class_number = input("Class number")
            self.school.enter_class(student_id, class_number)
        if option == 4:
            print "Exit a class"
            student_id = input("Student id")
            class_number = input("Class number")
            self.school.exit_class(student_id, class_number)
        if option == 5:
            print "Eating"
            student_id = input("Student id")
            self.school.get_student(student_id).eat()
        if option == 6:
            print "Chat"
            first_student_id = input("First student id")
            second_student_id = input("Second student id")
            self.school.chat(first_student_id, second_student_id)
        if option == 7:
            print "Students:"
            print self.school.students
        if option == 8:
            print "Teachers:"
            print self.school.teachers
        if option == 9:
            print "Whe ate in last 60 minutes?"
            eat_events = EventsLogger.events.get(EventTypes.EAT)
            if not eat_events:
                print "No one."
            else:
                eat_events.reverse()
                for eat_event in eat_events:
                    delta = datetime.now() - eat_event.creation_time
                    if delta.seconds / 60 > 60:
                        break
                    print eat_event.student.name
        if option == 10:
            print "Presence list"
            for klass in self.school.classes:
                print "Presence in {}:".format(klass.class_number)
                print klass.student_in_class_now