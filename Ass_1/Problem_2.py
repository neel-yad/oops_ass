def check_num(number):
    if(number%2==0):
        if(number in range(2,5) or (number>20)):
            print("Not Weird")
        elif(number in range(6,20)):
            print("Weird")
    else:
        print("Weird")
check_num(1)
check_num(3)
check_num(25)
check_num(24)
check_num(14)        