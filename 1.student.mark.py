# Function to get number of student/course
def get_number():
    Num = int(input("Enter the number: "))
    return Num

# Function to get the information of one student
# The list in this function refer to the student_list list in the get_multi_student_info function 
def get_one_student_info(list):
    id = input("Enter id of the student: ")
    name = input("Enter name of the student: ")
    dob = input("Enter DoB of the student: ")
    student_info = [id,name,dob]
    list.append(student_info)
 
# Function to get info of multiple students then list all of them
def get_multi_student_info():
    num_student = get_number()
    print("The number of students is: "+str(num_student))
    order_number=1
    student_list = []
    for i in range(num_student):
        print("Student "+str(order_number) +" information:")
        get_one_student_info(student_list)
        order_number+=1
    order_number=1   
        
    for student in student_list:
        print("Student "+str(order_number)+ " ID: " + str(student[0]) + ", Name: " + str(student[1]) + ", DoB: " + str(student[2]))
        order_number+=1
    return student_list

# Function to get the information of one course
# The use is similar to above functions
def get_one_course_info(list):
    course_id = input("Enter id of the course: ")
    course_name = input("Enter name of the course: ")
    course_info = [course_id,course_name]
    print(course_id +" "+ course_name)
    list.append(course_info)

# Function to get info of multiple courses then list all of them 
def get_multi_course_info():
    num_course = get_number()
    print("The number of course is: "+str(num_course))
    order_number=1
    course_list = []
    
    for i in range(num_course):
        print("Course "+str(order_number) +" information:")
        get_one_course_info(course_list)
        order_number+=1
    order_number=1    
    
    for course in course_list:
        print("Course "+str(order_number)+ " ID: " + str(course[0]) + ", Name: " + str(course[1]))
        order_number+=1
    return course_list

# Function to choose specific course then input mark of enrolled students
def input_mark(student_list, course_list):
    chosen_course = []

    course_id = input("Enter the course ID you'd like to input mark: ")
    
    for temp in course_list:
        print(course_id)
        if course_id == temp[0]:
            chosen_course = temp
            
    if not chosen_course:
        print("No info found")
        return
    
    for student in student_list:
        mark_input ={"Student" : str(chosen_course[0]) , "Mark" : float(input("Enter the student mark: "))}
        chosen_course.append(mark_input)

    for student in student_list:
        print("Course"+ str(chosen_course[0]) + str(student[0]) + str(chosen_course[2]))
        
# Main Program to build a student mark management system
student_list = get_multi_student_info()
course_list = get_multi_course_info()
input_mark(student_list,course_list)