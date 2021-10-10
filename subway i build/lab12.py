

class Salary:
    def __init__(self, pay):
        self.pay = pay
    def get_total(self):
        return (self.pay*12)
class Employee:
    def __init__(self, name, age ,pay, bonus):
        self.name=name
        self.age=age
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay)
    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() +self.bonus)
obj_emp = Employee( "ali", 35 ,600, 500)
print(obj_emp.annual_salary())