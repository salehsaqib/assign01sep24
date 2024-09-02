def chk_no(num):
    if num>=18:
        cnt_option:str =  input("Are you a Pakistani citizen?(yes/no): ")
        if (cnt_option=="yes"):
            print("You are eligible to vote")
        else:
            print("Please obtain a valid ID to vote.")   
    else:
        print("You are not eligible to vote.")   

unum:int =  int(input("Enter your age in years: "))
chk_no(unum)