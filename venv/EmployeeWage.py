import random

class Employee_Wage:
    WAGE_PER_HOUR = 20
    MAX_WORKING_DAYS = 20
    MAX_WORKING_HOURS = 100

    def calculate_working_hours(self,check_employee):
        IS_FULL_TIME = 1
        IS_PART_TIME = 2
        FULL_DAY = 8
        HALF_DAY = 4
        switcher = {
            IS_FULL_TIME: FULL_DAY ,
            IS_PART_TIME: HALF_DAY ,
        }
        return switcher.get(check_employee , 0)

    def calculate_employee_wage(self):
        working_days = 0
        total_working_hour = 0

        while working_days <= self.MAX_WORKING_DAYS and total_working_hour < self.MAX_WORKING_DAYS:
                check_employee = random.randint(0, 2)
                working_hour = self.calculate_working_hours(check_employee)
                working_days +=1
                total_working_hour += working_hour

        total_employee_wage = total_working_hour * self.WAGE_PER_HOUR
        print("The monthly wage of an employee is  :", total_employee_wage)

employee_wage = Employee_Wage()
employee_wage.calculate_employee_wage()