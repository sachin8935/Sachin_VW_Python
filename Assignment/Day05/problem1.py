
class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show_details(self):
        print(f"Company Name   : {self.name}")
        print(f"Location       : {self.location}")


class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    def show_details(self):
        print(f"Employee ID    : {self.emp_id}")
        print(f"Employee Name  : {self.emp_name}")
        print(f"Designation    : {self.designation}")



class CompanyAcquisition(Company):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_details(self):
        super().show_details()
        print("\n--- Employees After Acquisition ---")
        for emp in self.employees:
            print("\n---------------------------")
            emp.show_details()



class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date
        self.previous_company = previous_company

    def show_details(self):
        super().show_details()
        print(f"Joining Date   : {self.joining_date}")
        print(f"Previous Company: {self.previous_company}")


class Manager(NewEmployee):
    def __init__(self, emp_id, emp_name, joining_date, previous_company, team_size):
        super().__init__(emp_id, emp_name, "Manager", joining_date, previous_company)
        self.team_size = team_size

    def show_details(self):
        super().show_details()
        print(f"Team Size      : {self.team_size}")


class HR(NewEmployee):
    def __init__(self, emp_id, emp_name, joining_date, previous_company, policies_handled):
        super().__init__(emp_id, emp_name, "HR", joining_date, previous_company)
        self.policies_handled = policies_handled

    def show_details(self):
        super().show_details()
        print(f"Policies Handled: {self.policies_handled}")


class Developer(NewEmployee):
    def __init__(self, emp_id, emp_name, joining_date, previous_company, programming_languages):
        super().__init__(emp_id, emp_name, "Developer", joining_date, previous_company)
        self.programming_languages = programming_languages

    def show_details(self):
        super().show_details()
        print(f"Programming Languages: {', '.join(self.programming_languages)}")


class Intern(NewEmployee):
    def __init__(self, emp_id, emp_name, joining_date, previous_company, duration):
        super().__init__(emp_id, emp_name, "Intern", joining_date, previous_company)
        self.duration = duration

    def show_details(self):
        super().show_details()
        print(f"Internship Duration: {self.duration}")


class ManagerHR(Manager, HR):
    def __init__(self, emp_id, emp_name, joining_date, previous_company, team_size, policies_handled):
        NewEmployee.__init__(self, emp_id, emp_name, "Manager-HR", joining_date, previous_company)
        self.team_size = team_size
        self.policies_handled = policies_handled

    def show_details(self):
        NewEmployee.show_details(self)
        print(f"Team Size      : {self.team_size}")
        print(f"Policies Handled: {self.policies_handled}")


class DeveloperIntern(Developer, Intern):
    def __init__(self, emp_id, emp_name, joining_date, previous_company, programming_languages, duration):
        NewEmployee.__init__(self, emp_id, emp_name, "Developer Intern", joining_date, previous_company)
        self.programming_languages = programming_languages
        self.duration = duration

    def show_details(self):
        NewEmployee.show_details(self)
        print(f"Programming Languages: {', '.join(self.programming_languages)}")
        print(f"Internship Duration : {self.duration}")


if __name__ == "__main__":
    merged_company = CompanyAcquisition("TechFusion Ltd.", "Bangalore")

    # Employees
    emp1 = Manager(101, "Sachin", "2024-01-10", "OldSoft", 10)
    emp2 = HR(102, "Anita", "2023-12-05", "PeopleCorp", 5)
    emp3 = Developer(103, "Rahul", "2024-02-01", "CodeBase", ["Python", "Django"])
    emp4 = Intern(104, "Neha", "2024-06-01", "College", "6 Months")
    emp5 = ManagerHR(105, "Vikram", "2023-11-15", "HRTech", 8, 12)
    emp6 = DeveloperIntern(106, "Aman", "2024-07-01", "StartupX", ["Java", "Spring"], "3 Months")

    # Add employees to company
    merged_company.add_employee(emp1)
    merged_company.add_employee(emp2)
    merged_company.add_employee(emp3)
    merged_company.add_employee(emp4)
    merged_company.add_employee(emp5)
    merged_company.add_employee(emp6)

    # Display merged company details
    merged_company.show_details()
