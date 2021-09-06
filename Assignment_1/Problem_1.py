# Python program to check wheather a year is leap year or not
def leap_year(year):
    if((year%4==0)and(year%100!=0)and(year%400!=0)):
        print("Given Year is Leap Year")

    else:
        print("Given Year is not a Leap Year")
leap_year(5855)
leap_year(2000)
leap_year(1204)