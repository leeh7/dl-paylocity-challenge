# David Lee Paylocity Coding Challenge

Coding Challenge project for Paylocity SWE Interview

## Description

### Summary
Command line based Python program to calculate employee benefits cost

### Original Problem/Ask
One of the critical functions that we provide for our clients is the ability to pay for their employees’ benefits packages. A portion of these costs are deducted from their paycheck, and we handle that deduction. Please demonstrate how you would code the following scenario:
-   The cost of benefits is $1000/year for each employee
-   Each dependent (children and possibly spouses) incurs a cost of $500/year
-   Anyone whose name starts with ‘A’ gets a 10% discount, employee or dependent

We’d like to see this calculation used in a web application where employers input employees and their dependents, and get a preview of the costs.


### Solution
Using command-line menu based approach, program will take user input of Employee's first + last name and number of dependents (first + last name) per employee.

Factoring in Employee + dependents' names (discount condition mentioned above), program calculates total cost of benefits for all employees + their dependents entered in session before exiting program.

### Explanation/Reasoning of Approach

#### Planning
When starting out on this challenge/project, goal was to avoid pre-optimizing and get a working solution first, then make adjustments from there. 

Decided from there to make a menu-based command line application using Python for ease of setup/spinning up project to get working solution.

When planning structure of code for project, first task was to identify main entities/objects (thinking with OOP principles) being used to create needed classes based on the ask. 

From there, I identified the need for an Employee and Dependent class. Both classes share first + last name, but Employee class also includes `dependents` property to contain list of associated Dependents.


#### Main Program
I decided to use a menu-based approach operated via while loop given user input of three options: 
    -   enter employee, display entered employees 
    -   dependent info for current session, exit program
    -   show total benefits cost amount
  
`Option 1: ` If entering employee, program will prompt you to add employee first and last name, then ask for number of dependents for employee, and ask for first and last name of each dependent. 

`Note`: When entering first + last names, program will check that name inputs are letters only `(A-Z, a-z)` before proceeding (no numbers allowed).

`Option 2: ` Will display all employees and associated dependents entered in current session.

`Option 3: ` Exit program loop and calculate + output total cost of benefits for all employees and respectively associated dependents in dollar amount.






## Requirements
-   Python 3.9
-   Python packages:
    -   Babel (formatting dollar amount)
    -   typing (type hints for parameters)
        -   (ex. List of Employees)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip install babel typing
```

## Usage

```bash
python main.py
```

Enter `1`, `2`, or `3` at main menu to either add employee + dependents, display entered employees + dependents, or exit program and calculated total benefits cost.


## License
[MIT](https://choosealicense.com/licenses/mit/)