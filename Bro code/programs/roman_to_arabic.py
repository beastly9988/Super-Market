roman_symbols = ["I" , "V", "X", "L", "C", "D" , "M"  ]
roman_dict = {"I" : 1 , "V" : 5 , "X" : 10 , "L" : 50 , "C" : 100 ,  "D" :500 , "M" : 1000 }

while True:
    arab_num = []
    s = input("Ener the roman numberals:").upper()
    s =list(s)
    print(s)
    if  not all(elem in roman_symbols for elem in s):
        #  each element of s is checked whether it is in roman symbols or not.  second part only check if they are repeated or not roman numerical system dosent allow the repeating of those symbols 
        print("Invalid Input.")    
        continue
    if  s.count( "V" or "L" or "D" ) >= 2  :
        print("V or L or D can't be repeated in roman number system.")
        continue

    for num in s :
        arab_num.append(int(roman_dict[num]))
    print(arab_num)
    total = arab_num[0]    
    for idx , num in enumerate(arab_num) :
        try :
            if len(arab_num) <= 1 :
                total = arab_num[0]
                print(total)
                break
            elif arab_num[idx] > arab_num[idx +1] or arab_num[idx] == arab_num[idx +1] :
                total += arab_num[idx +1 ]
            elif arab_num[idx] < arab_num[idx +1] :
                total = total - arab_num[idx] + arab_num[idx +1] - arab_num[idx]
        except :
            print(total)
            break   
    break 