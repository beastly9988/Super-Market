menu = {
    "Momo"   : 150 ,
    "Burger" : 200 , 
    "Sausage": 40  ,
    "Pizza"  : 700 , 
    "Fries"  : 50  ,
}
Cart = []
total = 0

print("What would you like to buy?")
for key , value in menu.items() :
    print(f"{key} = {value}")
while True : 
    ch = input("Enter food (s to stop): ")
    item = menu.get(ch.capitalize())
    if ch.lower() == "s" :
        break
    quant = input("Enter quatity : ")
    while True : 
        if quant.isdigit() and int(quant) >0:
            quant = int(quant)
            break
        else:
            print("Invalid input.")
    if item :
        Cart.append(ch)
        total += item * quant
    else :
        print("Invalid input.")
print(f"Your total is ${total}")
