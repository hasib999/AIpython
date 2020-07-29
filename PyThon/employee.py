class Employee:
    empCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount += 1

    def displayInfo(self):
        print("Employee Name: %s   Employee Salary: %d" %(self.name,self.salary))

emp1=Employee("A",10000.00)
emp2=Employee("B",11000.00)
emp3=Employee("C",12000.00)
emp4=Employee("D",13000.00)
emp5=Employee("e",14000.00)

empList=[emp1,emp2,emp3,emp4,emp5]

for emp in empList:
    emp.displayInfo()











