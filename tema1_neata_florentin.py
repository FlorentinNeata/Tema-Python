class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        print(f"Nr total de angajati: {Employee.empCount}")

    def display_employee(self):
        print("Nume : ", self.name, ", Salariu: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        Manager.mgr_count += 1

    def display_employee(self):
        X = 5
        if X % 3 == 0:
            print(f"Name: {self.name}")
        elif X % 3 == 1:
            print(f"Salary: {self.salary}")
        elif X % 3 == 2:
            print(f"Department: {self.department}")

manager1 = Manager("Andrei Rusu", 60000, "F05_IT")
manager2 = Manager("Dan Daniel", 70000, "F05_HR")
manager3 = Manager("Ion Ionut", 80000, "F05_DevOps")
manager4 = Manager("Alexia Ioana", 75000, "F05_HQ")
manager5 = Manager("Emil Dumitru", 90000, "F05_QA")

for manager in [manager1, manager2, manager3, manager4, manager5]:
    manager.display_employee()

employee1 = Employee("Florentin Neata", 50000)
employee2 = Employee("Circiu Darius", 55000)

employee1.display_employee()
employee2.display_employee()

print("Nr de angajati:", employee1.empCount)
print("Nr de manageri:", manager1.mgr_count)
