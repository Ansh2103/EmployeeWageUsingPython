import random

class EmployeeWage:
    is_full_time = 1
    emp_rate_per_hour = 20
    #raandom.randint returns random value i.e; either 0 and 1
    emp_check = random.randint(0,1)

    #if emp_check = 1 (i.e; employee is present)
    #if emp_check = 0 (i.e ; employe is absent)
    if emp_check == is_full_time:
        working_hour = 8
    else:
        working_hour = 0

    #Calculating Employee Wage Of a Day
    employee_wage = working_hour * emp_rate_per_hour
    print("The Employee Wage Of A Day Is : ", employee_wage)