import random

class EmployeeWage:
    is_full_time = 1
    is_part_time = 2
    emp_rate_per_hour = 20
    #raandom.randint returns random value i.e; either 0, 1 or 2
    emp_check = random.randint(0,2)

    #if emp_check = 1 (i.e; employee is present)
    #if emp_check = 0 (i.e ; employe is absent)
    if emp_check == is_full_time :
        working_hour = 8
    elif emp_check == is_part_time :
        working_hour =4
    else:
        working_hour = 0

    #Calculating Employee Wage Of a Day
    employee_wage = working_hour * emp_rate_per_hour
    print("The Employee Wage Of A Day Is : ", employee_wage)