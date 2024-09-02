def pos_neg(num):
    if num<0:
        print(f"Number: {num} is a Negative Number")
    elif num>0:
        print(f"Number: {num} is a Positive Number")
    else: 
        print(f"Number: {num} is Zero")

unum:int =  int(input("Enter Number to check Positive, Negative or Zero: "))
pos_neg(unum)