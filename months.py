def chk_no(num):
    if (num==2):
        print("There are 28 Days in this month")
    elif (num==4) or (num==6) or (num==9) or (num==11):
        print("There are 30 Days in this month")
    elif (num==1) or (num==3) or (num==5) or (num==7) or (num==8)or (num==10)or (num==12):
        print("There are 31 Days in this month")
    else:
        print("Enter a valid Month Number (between 1-12)")    

unum:int =  int(input("Enter a month (as a number between 1 and 12): "))
chk_no(unum)