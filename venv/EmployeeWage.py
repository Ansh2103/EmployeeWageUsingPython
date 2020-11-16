import random

#constants and variables
IS_FULL_TIME = 1
IS_PART_TIME = 2
WAGE_PER_HOUR = 20
MAX_WORKING_DAYS = 20
MAX_WORKING_HOURS = 100
working_days = 0
working_hour = 0
total_working_hour = 0
daily_wage = 0
monthly_wage = 0

""" this function to calculate working hour of an employee """
def calculate_working_hours(check_employee):
    switcher = {
        IS_FULL_TIME: 8 ,
        IS_PART_TIME: 4 ,
    }
    return switcher.get(check_employee , 0)

while working_days <= MAX_WORKING_DAYS and total_working_hour < MAX_WORKING_HOURS:
    check_employee = random.randint(0, 2)
    working_hour = calculate_working_hours(check_employee)
    daily_wage = WAGE_PER_HOUR * working_hour
    monthly_wage += daily_wage
    working_days +=1
    total_working_hour += working_hour
print("The employee's Wage of a month is :", monthly_wage)
