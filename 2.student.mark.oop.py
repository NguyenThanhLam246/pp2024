class Init:
    def __init__(self):
        self.Name=input("Input name: ")
        self.ID=input("Input ID: ")
        
class Student(Init):
    def __init__(self):
        super().__init__()
        self.Dob=input("Input student DoB: ")
    
    def AddToList(self, studentList: list):
        studentList.append(self)
        
    def __str__(self):
        return f"ID: {self.ID}, Name: {self.Name}, DoB: {self.Dob}"

class Course(Init):
    def __init__(self):
        super().__init__()
        self._Mark={}
        
    def __str__(self):
        return  f"ID: {self.ID}, Name: {self.Name}"
    
    def InputMark(self, studentList:list):
        for student in studentList:
            self._Mark[student.ID] = {
                "Name": student.Name,
                "Mark": float(input(f"Input mark for {student.Name}: "))
            }
    def PrintMark(self):
        for key,value in self._Mark.items():
            print(f"Id: {key}, Name: {value['Name']}, Mark: {value['Mark']}")
    
def InputNumber(name):
    return int(input(f"Input number {name}"))

def SelectCourse(courseList, studentList)-> Course:
    if len(studentList) == 0 or len(courseList) == 0:
            print("Your student list or course list is empty")
    else:    
        PrintList(courseList)
        selectedID = input("Input the course ID of the course you want to choose: ")
        for course in courseList:
            if selectedID == course.ID:
                return course

def PrintList(list):
    for obj in list:
        print(obj)


studentNumber=0
courseNumber=0
studentList=[]
courseList=[]
    
while True:
    print("List of possible actions:\n \
        1. Input number of students in a class\n \
        2. Input student information\n \
        3. Input number of courses\n \
        4. Input course information\n \
        5. Select a course, input marks for student\n \
        6. Print course list\n \
        7. Print student list\n \
        8. Print student marks\n \
        9. Exit")
    action = int(input("Choose your action: "))
    
    if action == 1:
        studentNumber=InputNumber("of student:")
    elif action == 2:
        if studentNumber>0:
            for i in range(studentNumber):
                print(f"Input infor for student {i+1}")
                studentList.append(Student())
        else:
            print("You don't have number of student")
    elif action == 3:
        courseNumber=InputNumber("of course:")
    elif action == 4:
        if courseNumber>0:
            print(f"Input infor for course {i+1}")
            for i in range(courseNumber):
                courseList.append(Course())
        else:
            print("You don't have number of course")
    elif action == 5:
        selectedCourse = SelectCourse(courseList,studentList)
        if selectedCourse:
            selectedCourse.InputMark(studentList)
        else:
            print("Course not exist")        
    elif action == 6:
        if len(courseList) == 0:
            print("Your course list is empty")
        else:
            PrintList(courseList)
    elif action == 7:
        if len(studentList) == 0:
            print("Your student list is empty")
        else:
            PrintList(studentList)
    elif action == 8:
        selectedCourse = SelectCourse(courseList,studentList)
        if selectedCourse:
            selectedCourse.PrintMark()
        else:
            print("Course not exist") 
    elif action == 9:
        break
    else:
        print("Invalid choice")

    
    

    