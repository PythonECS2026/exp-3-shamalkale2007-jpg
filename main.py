

# Write your code here
# AIM: calculating gross salary of an employee
# Coder: Shamal
# Date: 26/1/2026
# Class: ECS/E2

print("Salary calculator")

BS = float(input("Enter the basic salary: "))

print()
print("Salary Details:")

print("Basic Salary:\t", BS)

DA = 0.70 * BS
print("DA (70%):\t", DA)

TA = 0.30 * BS
print("TA (30%):\t", TA)

HRA = 0.10 * BS
print("HRA (10%):\t", HRA)

GrossSalary = BS + DA + TA + HRA
print("Gross Salary:\t", GrossSalary)
