import random 
balance = 0
while True:
    ch = input("Would you like to add or withdraw money or  place bet ?(a/w/b) : ").lower()
    if ch not in ["a" , "w" , "b"] :
        print("Invalid Input.") 
        continue
    if ch == "a" :
        while True :
            add_sum =(input("Enter the amount you want to add : " ))
            if  not add_sum.isdigit() :
                print("Invalid Input.")
                continue
            else :
                add_sum = int(add_sum) 
                balance += add_sum
                break
    elif ch == "w" :
        while True :
            sub_sum =(input("Enter the amount you want to withdraw : " ))
            if  not sub_sum.isdigit() :
                print("Invalid Input.")
                continue
            elif int(sub_sum) > balance :
                print("Insufficient balance.")
                continue
            else :
                add_sum = int(add_sum) 
                balance += add_sum
                break 
    elif ch == "b" :
        while True :
            bet_sum =(input("Enter the amount you want to bet : " ))
            if  not bet_sum.isdigit() :
                print("Invalid Input.")
                continue
            elif int(bet_sum) > balance :
                print("Insufficient balance.")
                continue
            else :
                
