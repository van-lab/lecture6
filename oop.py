class Employee:
  raise_amount = 1.4
  number_of_employee = 0
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'
    self.number_of_employee += 1
    Employee.number_of_employee += 1

  def fullname(self):
    return(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

  @classmethod  # class declarator method
  def set_raise_amount(cls, amount):
    cls.raise_amount = amount

f = open("gentext.txt", "r")
for line in f:
  print(line)

f.close()

emp1 = Employee('van', 'san', 5000)
emp2 = Employee('ben', 'sen', 7000)

print(id(emp1))
print(id(emp2))


print(emp1.email)
print(emp1.fullname())
print(emp2.fullname())
print(f"before raise: {emp1.pay}")
print(f"raise amount = {emp1.raise_amount}")
Employee.set_raise_amount(1.05)
emp1.apply_raise()
print(f"new raise = {emp1.raise_amount}")
print(f"after raise: {emp1.pay}")
print(f"number of employee = {emp1.number_of_employee}")
print(f"number of employee = {Employee.number_of_employee}")
print(emp1.__dict__)
print(Employee.__dict__)