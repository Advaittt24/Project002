rooms = {
    '101': {'occupied': False, 'rate': 100},
    '102': {'occupied': False, 'rate': 120},
    '103': {'occupied': False, 'rate': 150},
}
    
print("Welcome to Cherrywood Lounge")

while True:
    print("\nOPTIONS")
    print("1.Book a room")
    print("2.Checkout")
    print("3.Exit")

    choice=input("Enter your choice (1-3): ")

    if choice=="1":
        room_number=input("Enter the room you would like to book: ")
        if room_number in rooms and not rooms[room_number]['occupied']:
                          print('Room number ' + str(room_number)+" booked successfully.")
                          rooms[room_number]['occupied']=True

        else:
            print("Sorry the room is not vacant or does not exist")


    elif choice=='2':
        room_number = input("Enter the room number for checkout: ")
        if room_number in rooms and rooms[room_number]['occupied']:
            print("Thank you for staying.")
            rooms[room_number]['occupied']= False
            total_bill=rooms[room_number]['rate']
            print("your total bill would be $"+str(total_bill))
            pay=input("yes/no: ")

            if pay=="yes":
             print("We hope you had a pleasant stay!")


            elif pay=="no":
                 print("kindly pay your bill")
             
            
            

    else:
        print("Exiting Cherrywood Lounge")
        break
