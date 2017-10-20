from Employee import *

e1 = Employee("seasonfif", 27)
e2 = Employee("season", 20)
e1.name = "qqq"
setattr(e1, "sex", "female")
getattr(e1, "sex")
e1.displayEmployee()
print Employee.empCount