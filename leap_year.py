def even_odd(num):
    if (num%4==0 and num%100!=0) or (num%400==0):
        print(f"Year: {num} is a Leap Year")
    else: 
        print(f"Year: {num} is a Non-Leap Year")

unum:int =  int(input("Enter Year to check for leap year or not: "))
even_odd(unum)