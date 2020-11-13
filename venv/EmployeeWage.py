import random

is_full_time = 1
is_part_time = 2
wage_per_hour = 20

#check whether employee is present or absent
# random.randint returns random value i.e; either 0, 1 or 2
check_employee = random.randint(0,2)
def calculate_working_hours(check_employee):
    switcher = {
        is_full_time: 8 ,
        is_part_time: 4 ,
    }
    return switcher.get(check_employee , 0)
#working hour of an employee
working_hours = calculate_working_hours(check_employee)

#calculate employee wage
employee_wage = working_hours * wage_per_hour
print ("Employee wage is : " , employee_wage)
