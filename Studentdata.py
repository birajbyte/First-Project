Students=[]

def add_student():
     id=int(input("Enter the student id   "))
     name=input("Enter the student name  ")
     age=int(input("Enter the age  "))
     course=input("Enter the course that student choose   ")

     student={
         "id":id,
         "name":name,
         "age":age,
         "course":course
     }
     Students.append(student)
     print("\nStudent data entered successfully")

def view_student():

    if not Students:
        print("Data donot found or not stored yet")
    else:
        print(f"{"id":<10}{"Name":<15}{"Age":<10}{"Course":<20}")
        print("-"*55)
        for  i in Students:
            print(f"{i["id"]:<10}{i["name"]:<15}{i["age"]:<10}{i["course"]:<25}")

def edit_data():
    edit_id=int(input("Enter the student id to edit   "))
    for i in Students:
        if i["id"]==edit_id:

            print(f"The old id is {i["id"]}")
            i["id"]=int(input("Enter the new id"))
            print(f"The old name is {i["name"]}")
            i["name"]=input("Enter the new name   ")
            print(f"Previous age of student is {i["age"]}")
            i["age"]=int(input("Enter the new age   "))
            print(f"Faculty previous  faculty {i["course"]}")
            i["course"]=input("Enter the new course joined   ")
            print("Data edited  successfully")
            return
    else:
        print("Student id not found")
       
def delete_data():
    delete_id=int(input("Enter the id of student to delete     "))
    for i in Students:
         if i["id"]==delete_id:
             
             print(f"id {i["id"]} name {"name"} age {"age"} course  {["course"]}")
             Students.remove(i)
             print("\nData removed successfully")
             return
    else:
        print("Student id not found")


def search_data():
    print("1.Search by name")
    print("2.Search by id")
    print("3.Search by age")
    choice=input("Enter the choice to search")
    if choice=="1":
        search_name=input("Search by name   ")
        for i in Students:
            if i["name"].lower()==search_name.lower():
                print(f"Required search  {i}")
    elif choice=="2":
        search_id=int(input("Search by id    "))
        for i in Students:
            if i["id"]==search_id:
                print(f"Requid result   {i}")
    elif choice=="3":
        search_age=int(input("Search by age   "))
        for i in Students:
            if i["age"]==search_age:
                print(f"Required search  {i}")
    else:
        print("Search not found")
        
while True:
    print("\nStudent Management System")

    print("\n1.Add Student")
    print("2.View Student")
    print("3.Edit Student")
    print("4.Delete Student Data")
    print("5.Search Data")
    print("6.Exit Data Entry")

    user_decision=input("Enter the choice you want to make ")
    if user_decision=="1":
        add_student()
    elif user_decision=="2":
        view_student()
    elif user_decision=="3":
        edit_data()
    elif user_decision=="4":
        delete_data()
    elif user_decision=="5":
        search_data()
    elif user_decision=="6":
        break
    else:
        print("Make the correct choice 1 to 6")





   





    







