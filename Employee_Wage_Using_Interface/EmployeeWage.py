import random

from Employee_Wage_Using_Interface.Interface_Employee_Wage import Inteface_Employee_Wage

class Employee_Wage(Inteface_Employee_Wage):
    IS_FULL_TIME = 1
    IS_PART_TIME = 2
    FULL_DAY = 8
    HALF_DAY = 4

    def __init__(self,name,WAGE_PER_HOUR,MAX_WORKING_DAYS,MAX_WORKING_HOURS):
        '''
            Parameters:
                name = company's name
                WAGE_PER_HOUR = the amount getting paid of an employee per hour
                MAX_WORKING_DAYS : maximum working day limit of an employee in a month
                MAX_WORKING_HOURS : maximum working hours limit of an employee in a month

                __init__ : it is the constructor method in python ;
                                  it is called whenever an object of  class is constucted.
            '''
        self.name = name
        self.WAGE_PER_HOUR = WAGE_PER_HOUR
        self.MAX_WORKING_DAYS = MAX_WORKING_DAYS
        self.MAX_WORKING_HOURS = MAX_WORKING_HOURS

    def __str__(self):
        return "{} {} {} {}".format(self.name,self.WAGE_PER_HOUR,self.MAX_WORKING_DAYS,self.MAX_WORKING_HOURS)

    def calculate_working_hours(self,check_employee):
        '''
                Checking whether employee is Full_Time, Part Time or Absent
                if  1: Full time
                    2: Half time
                    3: Absent
                    '''
        switcher = {
            self.IS_FULL_TIME: self.FULL_DAY,
            self.IS_PART_TIME: self.HALF_DAY,
        }
        return switcher.get(check_employee, 0)

    def calculate_employee_wage(self):
        '''
               Calculating the monthly wage of an employee
        '''
        working_days = 0
        working_hour = 0
        total_working_hour = 0

        while working_days <= self.MAX_WORKING_DAYS and total_working_hour < self.MAX_WORKING_HOURS:
                check_employee = random.randint(0, 2)
                working_hour = self.calculate_working_hours(check_employee)
                working_days +=1
                total_working_hour += working_hour

        total_employee_wage = total_working_hour * self.WAGE_PER_HOUR
        print("The monthly wage of an employee in the ",self.name,"of a month is : ",total_employee_wage)

        '''
       creating object of the respective company and returning arguments as
       ("CompanyName",WAGE_PER_HOUR,MAX_WORKING_DAYS,MAX_WORKING_HOURS)
     '''
def list():
    list_of_companies = []
    DMart = Employee_Wage("DMart",20,31,80)
    Reliance = Employee_Wage("Reliance",40,28,90)
    flipcart = Employee_Wage("flipcart",30,30,100)
    list_of_companies.append(DMart)
    list_of_companies.append(Reliance)
    list_of_companies.append(flipcart)
    DMart.calculate_employee_wage()
    Reliance.calculate_employee_wage()
    flipcart.calculate_employee_wage()

    for list_object in list_of_companies:
      print(list_object)

if __name__ == '__main__':
    list()


