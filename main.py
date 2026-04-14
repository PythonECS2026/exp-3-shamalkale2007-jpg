# Write your code here
# AIM: calculating gross salary of an employee
# Coder: Shamal
# Date: 26/1/2026
# Class: ECS/E2
BS = float(input())

DA = 0.7 * BS
TA = 0.3 * BS
HRA = 0.1 * BS
GS = BS + DA + TA + HRA

print("Salary Details:")
print(f"Basic Salary:\t{BS}")
print(f"DA (70%):\t{DA}")
print(f"TA (30%):\t{TA}")
print(f"HRA (10%):\t{HRA}")
print(f"Gross Salary:\t{GS}")
