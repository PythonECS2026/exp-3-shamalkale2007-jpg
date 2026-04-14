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
print("Basic Salary:\t\t{:.1f}".format(BS))
print("DA (70%):\t\t{:.1f}".format(DA))
print("TA (30%):\t\t{:.1f}".format(TA))
print("HRA (10%):\t\t{:.1f}".format(HRA))
print("Gross Salary:\t\t{:.1f}".format(GS))
