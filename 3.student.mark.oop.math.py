import math
import numpy as np
import curses

class Student:
    def __init__(self, s_id, name, dob):
        self.s_id = s_id
        self.name = name
        self.dob = dob
        self.mark = {}
        self.gpa = 0

    def get_id(self):
        return self.s_id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def add_mark(self, course_id, mark):
        self.mark[course_id] = mark

    def get_marks(self):
        return self.mark

    def calculate_gpa(self, courses, credits):
        marks = np.array([self.mark.get(course, 0) for course in courses])
        gpa = np.sum(marks * credits) / np.sum(credits)
        self.gpa = gpa
        return gpa

class Course:
    def __init__(self, c_id, c_name, credits):
        self.c_id = c_id
        self.c_name = c_name
        self.credits = credits

    def get_c_id(self):
        return self.c_id

    def get_c_name(self):
        return self.c_name

    def get_credits(self):
        return self.credits

class SystemManagement:
    def __init__(self):
        self.students_list = []
        self.courses_list = []

    def input_s_info(self, stdscr):
        num = int(input("Enter the number of students: "))
        for i in range(num):
            s_id = input("Enter the student id: ")
            name = input("Enter the student name: ")
            dob = input("Enter the student dob: ")
            student = Student(s_id, name, dob)
            self.students_list.append(student)

    def input_c_info(self, stdscr):
        num = int(input("Enter the number of courses: "))
        for i in range(num):
            c_id = input("Enter the course id: ")
            c_name = input("Enter the course name: ")
            credits = int(input("Enter the credits for this course: "))
            course = Course(c_id, c_name, credits)
            self.courses_list.append(course)

    def input_marks(self, stdscr):
        course_id = input("Enter the id of the course that you want to input marks for: ")
        for student in self.students_list:
            mark = float(input(f"Enter the mark for {student.get_name()}: "))
            mark = math.floor(mark * 10) / 10  # Round down to 1 decimal place
            student.add_mark(course_id, mark)

    def show_students_list(self, stdscr):
        for student in self.students_list:
            print(f"Student ID: {student.get_id()}, Name: {student.get_name()}, DoB: {student.get_dob()}")

    def show_courses_list(self, stdscr):
        for course in self.courses_list:
            print(f"Course ID: {course.get_c_id()}, Course Name: {course.get_c_name()}, Credits: {course.get_credits()}")

    def show_course_mark(self, stdscr):
        course_id = input("Enter the id of the course that you want to search: ")
        for student in self.students_list:
            marks = student.get_marks()
            if course_id in marks:
                print(f"Student ID: {student.get_id()}, Name: {student.get_name()}, Mark: {marks[course_id]}")

    def calculate_and_sort_gpa(self, stdscr):
        courses = [course.get_c_id() for course in self.courses_list]
        credits = np.array([course.get_credits() for course in self.courses_list])

        for student in self.students_list:
            student.calculate_gpa(courses, credits)

        # Sort students by GPA in descending order
        self.students_list.sort(key=lambda student: student.gpa, reverse=True)

    def show_sorted_students_by_gpa(self, stdscr):
        self.calculate_and_sort_gpa(stdscr)
        print("Students sorted by GPA:")
        for student in self.students_list:
            print(f"Student ID: {student.get_id()}, Name: {student.get_name()}, GPA: {student.gpa:.2f}")


def main(stdscr):
    system = SystemManagement()
    while True:
        stdscr.clear()
        stdscr.addstr("\nOptions:\n")
        stdscr.addstr("1. Input students\n")
        stdscr.addstr("2. Input courses\n")
        stdscr.addstr("3. Input marks for a course\n")
        stdscr.addstr("4. List students\n")
        stdscr.addstr("5. List courses\n")
        stdscr.addstr("6. Show student marks for a course\n")
        stdscr.addstr("7. Show sorted students by GPA\n")
        stdscr.addstr("8. Exit\n")

        stdscr.addstr("Enter your choice: ")
        stdscr.refresh()
        choice = int(stdscr.getstr().decode())

        if choice == 1:
            system.input_s_info(stdscr)
        elif choice == 2:
            system.input_c_info(stdscr)
        elif choice == 3:
            system.input_marks(stdscr)
        elif choice == 4:
            system.show_students_list(stdscr)
        elif choice == 5:
            system.show_courses_list(stdscr)
        elif choice == 6:
            system.show_course_mark(stdscr)
        elif choice == 7:
            system.show_sorted_students_by_gpa(stdscr)
        elif choice == 8:
            break
        else:
            stdscr.addstr("Invalid choice\n")
            stdscr.refresh()
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
