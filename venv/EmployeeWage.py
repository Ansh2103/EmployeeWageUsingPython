import random

#constants and variables
is_full_time = 1
is_part_time = 2
wage_per_hour = 20
max_working_day = 20
max_working_hour = 100
working_days = 0
working_hour = 0
total_working_hour = 0
daily_wage = 0
monthly_wage = 0

""" this function to calculate working hour of an employee """
def calculate_working_hours(check_employee):
    switcher = {
        is_full_time: 8 ,
        is_part_time: 4 ,
    }
    return switcher.get(check_employee , 0)

while working_days <= max_working_day and total_working_hour < max_working_hour:
    check_employee = random.randint(0, 2)
    working_hour = calculate_working_hours(check_employee)
    daily_wage = wage_per_hour * working_hour
    monthly_wage += daily_wage
    working_days +=1
    total_working_hour += working_hour
print("The employee's Wage of a month is :", monthly_wage)
