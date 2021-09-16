def guest1(guest_list,name):
    length=len(guest_list)
    position_name=guest_list.index(name)
    if(position_name>=int((length/2))):
        print("Fashionably Late")
    else:
        print("Not Fashionably Late")    
guest_list=["Neeraj","Atharv","Pankaj","Pritesh","Praveen","Avadesh","Rajesh"]
guest1(guest_list,"Neeraj")
guest1(guest_list,"Atharv")
guest1(guest_list,"Pankaj")
guest1(guest_list,"Pritesh")
guest1(guest_list,"Praveen") 
guest1(guest_list,"Avadesh")
guest1(guest_list,"Rajesh")