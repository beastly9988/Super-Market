"""
Input principal , rate , time , n
calculate interest (formula) =[ A = P * (1 + r / n) ** (n * t)]    [CI = A - P] { A = P * (1 + r) ** t  CI = A - P}
print CI
"""
p = 0 # Also just use While True instead of using the condition
t = 0 
r = 0 
while p<=0 :
    p = int(input("Enter Principle: "))
    if p <= 0 :
        print("Invalid input (Must be positive number.)")
while r<=0 or r> 100 :
    r = float(input("Enter Rate: "))
    if r <= 0 or r> 100 :
        print("Invalid input (Must be positive number and from 1 to 100 .)")
while t<=0 :
    t = float(input("Enter Time (years): "))
    if t <= 0 :
        print("Invalid input (Must be positive number.)")


a = p * (1 + r) ** t
CI = a - p 
print(f"The compund interest is : ${CI}")

