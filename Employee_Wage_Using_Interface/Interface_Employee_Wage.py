from abc import ABC, abstractmethod

class Inteface_Employee_Wage:

    @abstractmethod
    def calculate_employee_wage(self):
        pass

    @abstractmethod
    def calculate_working_hours(self, check_employee):
        pass