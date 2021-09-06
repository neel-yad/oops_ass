def guest1(guest_list,name):
    length=len(guest_list)
    position_name=guest_list.index(name)
    if(position_name>=int((length/2))):
        print("Fashionably Late")
    else:
        print("Not Fashionably Late")    
guest_list=["Neeraj Yadav","Atharv Yadav","Pankaj Yadav","Pritesh Yadav","Praveen Yadav","Avadesh Yadav","Rajesh Yadav"]
guest1(guest_list,"Neeraj Yadav")
guest1(guest_list,"Atharv Yadav")
guest1(guest_list,"Pankaj Yadav")
guest1(guest_list,"Pritesh Yadav")
guest1(guest_list,"Praveen Yadav") 
guest1(guest_list,"Avadesh Yadav")
guest1(guest_list,"Rajesh Yadav")