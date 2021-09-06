def gross_pay(BP):
    DA=(BP*40)/100
    HRA=(BP*20)/100
    GP=BP+HRA+DA
    print("Gross Pay of Employee is %f"%GP)
gross_pay(2568)
gross_pay(100)