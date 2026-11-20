# Q4. Employee Salary Calculator using Function Arguments
# Create a function:
# calculate_salary(basic_salary, bonus=2000)
# The function should calculate and display:
# Total Salary = Basic Salary + Bonus
# Demonstrate the use of:
# • Positional Arguments
# • Keyword Arguments
# • Default Arguments


def calculate_salary(basic_salary, bonus=2000):
    total_salary = basic_salary + bonus
    return total_salary

salary1 = calculate_salary(30000, 2000)   # Positional Arguments
print("Employee 1 Salary:", salary1)

salary2 = calculate_salary(basic_salary=33000, bonus=2000)     # Keyword Arguments
print("Employee 2 Salary:", salary2)

salary3 = calculate_salary(25000)       # Default Arguments
print("Employee 3 Salary:", salary3)
