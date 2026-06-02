class Employee:

    def _init_(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("------------------------")


employees = []


def add_employee():

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Salary: ")

    emp = Employee(emp_id, name, salary)

    employees.append(emp)

    print("Employee Added Successfully!")


def view_employees():

    if len(employees) == 0:
        print("No Employees Found")
        return

    for emp in employees:
        emp.display()


def search_employee():

    emp_id = input("Enter Employee ID to Search: ")

    for emp in employees:
        if emp.emp_id == emp_id:
            print("Employee Found")
            emp.display()
            return

    print("Employee Not Found")


def delete_employee():

    emp_id = input("Enter Employee ID to Delete: ")

    for emp in employees:
        if emp.emp_id == emp_id:
            employees.remove(emp)
            print("Employee Deleted Successfully")
            return

    print("Employee Not Found")


while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
