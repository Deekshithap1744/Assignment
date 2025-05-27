# class Employee:
#     def __init__(self):
#         self.Name="Deekshitha"
#         self.age=21
#         self.job="Data Analyst"
#     def getEmployee(self):
#         print("Employee Information")
#         print("---------------------")
#         print(f"Name:{self.Name}")
#         print(f"Age:{self.age}")
#         print(f"Job:{self.job}")
# emp1=Employee()
# emp1.getEmployee()

#Where name is not defined in the function, but defined in the object
# class Employee:
#     def __init__(self,Name,age,job): # whenever there is a self in function parameters then,its called as "Instance method"
#         self.Name=Name
#         self.age=age 
#         self.job=job
#     def getEmployee(self):
#         print("Employee Information")
#         print("---------------------")
#         print(f"Name:{self.Name}")
#         print(f"Age:{self.age}")
#         print(f"Job:{self.job}")
# emp1=Employee("Chinnu",22,"Data Analyst")
# emp1.getEmployee()
# emp2=Employee("Ladduu",18,"Test Engineer")
# emp2.getEmployee()

#class-level variable: its returned outside the function to increase the emp count and can be used by all the methods in a class

# class Employee:
#     employee_count=0
#     def __init__(self,Name,age,job): # whenever there is a self in function parameters then,its called as "Instance method"
#         self.Name=Name
#         self.age=age 
#         self.job=job
#         Employee.employee_count+=1
        
#     def getEmployee(self):
#         print("Employee Information")
#         print("---------------------")
#         print(f"Name:{self.Name}")
#         print(f"Age:{self.age}")
#         print(f"Job:{self.job}")
        
#     @classmethod
#     def total_emp(cls):
#         return cls.employee_count
# emp1=Employee("Chinnu",22,"Data Analyst")
# emp1.getEmployee()
# emp2=Employee("Ladduu",18,"Test Engineer")
# emp2.getEmployee()
# print(f"Total Employees:{Employee.total_emp()}") ##by using a class name, we get the total count


#create class as department, dept id ,dept name,location,hod,no.of depts through the constructor initialise the different depts,attributes
# create a method to display important informaation,display total depts in your organization
# take input from user, store all info in the list,tuple or dictionary
#search department by dept id,if valid give all the info, if not say not valid
# add a function to search dept by name,implement search by name functionality



class Department:
    dept_count = 0
    l = []

    def __init__(self):
        self.DepartmentId = int(input("Enter the Department Id: "))
        self.DeptName = input("Enter the Department Name: ")
        self.Location = input("Enter the Location: ")
        self.Hod = input("Enter the Head of the Department: ")
        Department.dept_count += 1
        Department.l.append(self)

    def getDept_details(self):
        print("\nDepartment Information")
        print("--------------------------------------")
        print(f"Department Id: {self.DepartmentId}")
        print(f"Department Name: {self.DeptName}")
        print(f"Location: {self.Location}")
        print(f"Head of the Department: {self.Hod}")

    @classmethod
    def total_dept(cls):
        return cls.dept_count

    @classmethod
    def search_by_id(cls, DepartmentId):
        for dept in cls.l:
            if dept.DepartmentId == DepartmentId:
                dept.getDept_details()
                return
        print("Invalid Id")

    @classmethod
    def search_by_name(cls, DeptName):
        for dept in cls.l:
            if dept.DeptName.lower() == DeptName.lower():
                dept.getDept_details()
                return
        print("No name Exists")

n = int(input("How many departments do you want to add? "))


for i in range(n):
    print(f"\nEntering details for Department {i + 1}")
    dept_obj = Department()

print("\nDisplaying first department details:")
Department.l[0].getDept_details()
print(f"\nTotal Departments: {Department.total_dept()}")

print("\n--- Search Options ---")
option = input("Search by ID or Name? (id/name): ").strip().lower()
if option == "id":
    DeptId = int(input("Enter ID to search: "))
    Department.search_by_id(DeptId)
elif option == "name":
    DeptName = input("Enter Name to search: ")
    Department.search_by_name(DeptName)
else:
    print("Invalid choice.") 

        
        
        
        
        














        