<<<<<<< HEAD
class Student:
    def __init__(self, s_id, name, dob):
        self.s_id = s_id
        self.name = name
        self.dob = dob
        self.mark = {}

    def get_id(self):
        return self.s_id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def add_mark(self, course_id, mark):
        self.mark[course_id] = mark

    def get_marks(self):
        return self.mark  # Fixed typo


class Course:
    def __init__(self, c_id, c_name):
        self.c_id = c_id
        self.c_name = c_name

    def get_c_id(self):
        return self.c_id

    def get_c_name(self):
        return self.c_name


class SystemManagement:
    def __init__(self):
        self.students_list = []
        self.courses_list = []

    def input_s_info(self):
        num = int(input("Enter the number of students: "))
        for i in range(num):
            s_id = input("Enter the student id: ")
            name = input("Enter the student name: ")
            dob = input("Enter the student dob: ")
            student = Student(s_id, name, dob)  # Fixed instance creation
            self.students_list.append(student)  # Append instance

    def input_c_info(self):
        num = int(input("Enter the number of courses: "))
        for i in range(num):
            c_id = input("Enter the course id: ")
            c_name = input("Enter the course name: ")
            course = Course(c_id, c_name)  # Fixed instance creation
            self.courses_list.append(course)  # Append instance

    def input_marks(self):
        course_id = input("Enter the id of the course that you want to input mark: ")
        for student in self.students_list:
            mark = input(f"Enter the mark for {student.get_name()}: ")  # Removed self
            student.add_mark(course_id, mark)

    def show_students_list(self):
        for student in self.students_list:
            print(f"Student ID: {student.get_id()}, Name: {student.get_name()}, DoB: {student.get_dob()}")

    def show_courses_list(self):
        for course in self.courses_list:
            print(f"Course ID: {course.get_c_id()}, Course Name: {course.get_c_name()}")

    def show_course_mark(self):
        course_id = input("Enter the id of the course that you want to search: ")
        for student in self.students_list:
            marks = student.get_marks()
            if course_id in marks:
                print(f"Student ID: {student.get_id()}, Name: {student.get_name()}, Mark: {marks[course_id]}")

def main():
    system = SystemManagement()
    while True:
        print("\nOptions:")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a course")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            system.input_s_info()
        elif choice == 2:
            system.input_c_info()
        elif choice == 3:
            system.input_marks()
        elif choice == 4:
            system.show_students_list()
        elif choice == 5:
            system.show_courses_list()
        elif choice == 6:
            system.show_course_mark()
        elif choice == 7:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

    
>>>>>>> d5516a6bf8074790730577a93ee75974a2765488
