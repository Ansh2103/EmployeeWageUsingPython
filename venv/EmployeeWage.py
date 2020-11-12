import math
import random

class EmployeeWage:
    is_full_time = 1
    emp_check = random.randint(0,1)

    if emp_check == is_full_time:
        print("Employee is present")
    else:
        print("Employee is Absent")