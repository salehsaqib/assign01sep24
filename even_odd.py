def even_odd(num):
    if num%2==0:
        print(f"Number: {num} is an even Number")
    else: 
        print(f"Number: {num} is an odd Number")

unum:int =  int(input("Enter Number to check Even or Odd: "))
even_odd(unum)