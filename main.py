# Write your code here
# AIM: calculating gross salary of an employee
# Coder: Shamal
# Date: 26/1/2026
# Class: ECS/E2
print("Salary  Details:")
BS = float(input("Basic Salary:5000 "))
DA = 0.70*BS
TA = 0.3*BS
HRA = 0.10*BS
GS = BS+DA+TA+HRA
print(f"DA(70%): {DA: .1f} ")
print(f"TA(30%): {TA: .1f} ")
print(f"HRA(10%): {HRA: .1f} ")
print(f"Gross Salary: {GS: .1f} ")


