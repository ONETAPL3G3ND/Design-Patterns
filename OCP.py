from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calculate_pay(self) -> float:
        pass

class PermanentEmployee(Employee):
    def __init__(self, name: str, monthly_salary: float):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self) -> float:
        return self.monthly_salary

class ContractEmployee(Employee):
    def __init__(self, name: str, hourly_rate: float, hours_worked: int):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self) -> float:
        return self.hourly_rate * self.hours_worked

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def calculate_total_pay(self) -> float:
        total_pay = 0.0
        for employee in self.employees:
            total_pay += employee.calculate_pay()
        return total_pay
