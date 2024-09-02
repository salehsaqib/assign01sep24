def chk_no(num):
    if (num<=0) or (num>=125):
        print("Enter a valid age")
    elif (num>0) and (num<=12):
        print("you are a child")
    elif (num>12) and (num<=19):
        print("you are a teenager")
    elif (num>19) and (num<=59):
        print("you are an adult")
    elif (num>59) and (num<125):
        print("you are a senior citizen")    

unum:int =  int(input("Enter your age in years: "))
chk_no(unum)