from models.department import Department
from models.employee import Employee

def exit_program():
    print("Goodbye!")
    exit()

# Department functions are already implemented
def list_departments():
    """List all departments."""
    departments = Department.get_all()
    for department in departments:
        print(department)

def find_department_by_name():
    """Find a department by name."""
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f'Department {name} not found')

def find_department_by_id():
    """Find a department by id."""
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')

def create_department():
    """Create a new department."""
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)

def update_department():
    """Update an existing department."""
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')

def delete_department():
    """Delete a department by id."""
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')

# Employee functions to implement

def list_employees():
    """List all employees."""
    employees = Employee.get_all()  # Assuming you have a similar method for employees
    for employee in employees:
        print(employee)

def find_employee_by_name():
    """Find an employee by name."""
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)  # Adjust for your ORM
    print(employee) if employee else print(f'Employee {name} not found')

def find_employee_by_id():
    """Find an employee by id."""
    id_ = input("Enter the employee's id: ")
    try:
        id_ = int(id_)
        employee = Employee.find_by_id(id_)  # Adjust for your ORM
        print(employee) if employee else print(f'Employee {id_} not found')
    except ValueError:
        print("Invalid employee id")

def create_employee():
    """Create a new employee."""
    try:
        name = input("Enter the employee's name: ")
        job_title = input("Enter the employee's job title: ")
        department_id = input("Enter the employee's department id: ")

        # Validate inputs
        if not name:
            raise ValueError("Name must be a non-empty string")
        if not job_title:
            raise ValueError("Job title must be a non-empty string")

        department = Department.find_by_id(department_id)  # Adjust for your ORM
        if not department:
            raise ValueError("department_id must reference a department in the database")

        employee = Employee.create(name, job_title, department_id)  # Adjust for your ORM
        print(f"Success: {employee}")

    except ValueError as e:
        print(f"Error creating employee: {e}")
    except Exception as e:
        print(f"Error creating employee: {e}")

def update_employee():
    """Update an existing employee."""
    id_ = input("Enter the employee's id: ")
    try:
        id_ = int(id_)
        employee = Employee.find_by_id(id_)  # Adjust for your ORM

        if not employee:
            print(f"Employee {id_} not found")
            return

        name = input("Enter the employee's new name: ")
        job_title = input("Enter the employee's new job title: ")
        department_id = input("Enter the employee's new department id: ")

        # Validate inputs
        if name:
            employee.name = name
        if job_title:
            employee.job_title = job_title
        if department_id:
            department = Department.find_by_id(department_id)  # Adjust for your ORM
            if not department:
                raise ValueError("department_id must reference a department in the database")
            employee.department_id = department_id

        employee.update()  # Adjust for your ORM
        print(f"Success: {employee}")

    except ValueError as e:
        print(f"Error updating employee: {e}")
    except Exception as e:
        print(f"Error updating employee: {e}")

def delete_employee():
    """Delete an employee by id."""
    id_ = input("Enter the employee's id: ")
    try:
        id_ = int(id_)
        employee = Employee.find_by_id(id_)  # Adjust for your ORM
        if employee:
            employee.delete()  # Adjust for your ORM
            print(f"Employee {id_} deleted")
        else:
            print(f"Employee {id_} not found")
    except Exception as e:
        print(f"Error deleting employee: {e}")

def list_department_employees():
    """List all employees in a department."""
    dept_id = input("Enter the department's id: ")
    try:
        dept_id = int(dept_id)
        department = Department.find_by_id(dept_id)  # Adjust for your ORM
        if department:
            employees = department.get_employees()  # Assuming a method that returns employees
            for employee in employees:
                print(employee)
        else:
            print(f"Department {dept_id} not found")
    except ValueError:
        print("Invalid department id")
    except Exception as e:
        print(f"Error listing department employees: {e}")
