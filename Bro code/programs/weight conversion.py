ch = input("""1. Kg to Lbs
2.Lbs to Kg
Enter the conversion required (1,2):""")
if ch == "1":
    unit = "kg"
    unit1 = "lbs"
elif ch == "2" :
    unit = "lbs"
    unit1 = "kg"
else :
    print("Ivalid input.")

weight= float(input(f"Enter the weight in {unit}"))
if ch == "1" :
    new_weight = weight /0.453592
elif ch == "2" :
    new_weight = weight*0.453592
else :
    print("Ivalid input.")

print(f"The weight in {unit1} is {round(new_weight,2)}{unit1}.")

    