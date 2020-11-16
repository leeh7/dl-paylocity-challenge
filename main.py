from dependant import Dependent
from employee import Employee
from typing import List
from babel.numbers import format_currency

def main():
    #   store employees created in session, reset on exit
    employee_list = []

    print("Welcome to the Employee Benefits Calculator!")

    user_input = ""

    while user_input != "quit" or user_input == 3:

        print("""
        Main Menu:
        -   To enter an employee's benefits, press 1
        -   To preview currently entered employees and dependents, press 2
        -   To Exit and show all employees + calculated benefits, press 3
        """)
        user_input = int(input("Please enter a selection number: "))

        if user_input == 1:
            curr_employee = Employee()
            #   need to ensure employee + dependent names only contain letters
            while True:
                emp_first_name = input("Please enter employee's first name: ")
                emp_last_name = input("Please enter employee's last name: ")
                if emp_first_name.isalpha() and emp_last_name.isalpha():
                    break
                print("first and/or last name is invalid, please enter again")
            emp_dep_count = int(input("Please enter number of dependents for this employee: "))
            if emp_dep_count > 0:
                dep_count = 0
                while dep_count < emp_dep_count:
                    curr_dependent = Dependent()
                    dep_first_name = dep_last_name = ""
                    while True:
                        dep_first_name = input("Please enter dependent {}'s first name: ".format(dep_count + 1))
                        dep_last_name = input("Please enter dependent {}'s last name: ".format(dep_count + 1))
                        if dep_first_name.isalpha() and dep_last_name.isalpha():
                            break
                        print("first and/or last name is invalid, please enter again")
                    curr_dependent.first_name = dep_first_name
                    curr_dependent.last_name = dep_last_name
                    curr_employee.add_dependant(curr_dependent)
                    dep_count += 1

            curr_employee.first_name = emp_first_name
            curr_employee.last_name = emp_last_name
            employee_list.append(curr_employee)
        
        elif user_input == 2:
            output_info(employee_list)
        elif user_input == 3:
            break
        else:
            print("Invalid choice, please try again. \n")

    total_benefit_cost = calculate_employee_benefits_total(employee_list)
    total_benefit_cost_str = format_currency(   total_benefit_cost, 
                                                "USD", 
                                                locale="en_US", 
                                                format="$#,###.00") 
    print("Total cost of benefits for all employees in this session is: " + total_benefit_cost_str)

def calculate_employee_benefits_one(employee: Employee) -> int:
    #   gathering variables/values to be used
    pay_per_paycheck = 2000
    total_pay_before_deductions = pay_per_paycheck * 26
    annual_employee_benefits_cost = (1000 * .9) if check_for_discount(employee.first_name, employee.last_name) else 1000
    cost_per_dependent = 500
    dependents_total_cost = 0

    #   calculate total cost of benefits for dependents of employee
    for dependent in employee.dependents:
        if check_for_discount(dependent.first_name, dependent.last_name):
            dependents_total_cost += cost_per_dependent * .9
        else:
            dependents_total_cost += cost_per_dependent
    employee_total_benefit_cost = total_pay_before_deductions - annual_employee_benefits_cost - dependents_total_cost
    
    return employee_total_benefit_cost

def check_for_discount(first_name: str, last_name: str) -> bool:
    if first_name[0].upper() == 'A' or last_name[0].upper() == 'A':
        return True
    return False

# NEED output method/print method
def output_info(employees: List[Employee]) -> None:
    if len(employees) < 1:
        print("No Employees entered, please enter employees\n")
        return
    
    for employee in employees:
        employee.output_employee_info()

def calculate_employee_benefits_total(employees: List[Employee]) -> int:
    employees_benefit_cost = 0
    for employee in employees:
        employees_benefit_cost += calculate_employee_benefits_one(employee)
    return employees_benefit_cost

if __name__ == "__main__":
    main()