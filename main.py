# AIM: Write a Python program to calculate the gross salary of an employee.
# Coder:shamal
# Date:26th Jan 26

# Write your code here
basic_salary = 5000.0

da = basic_salary * 0.70      # 70%
ta = basic_salary * 0.30      # 30%
hra = basic_salary * 0.10     # 10%

gross_salary = basic_salary + da + ta + hra

print("Salary Details:")

print("Basic Salary:")
print(basic_salary)

print("DA (70%):")
print(da)

print("TA (30%):")
print(ta)

print("HRA (10%):")
print(hra)

print("Gross Salary:")
print(gross_salary)
