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
print(f"Basic Salary:    {basic_salary}")
print(f"DA (70%):        {da}")
print(f"TA (30%):        {ta}")
print(f"HRA (10%):       {hra}")
print(f"Gross Salary:    {gross_salary}")
