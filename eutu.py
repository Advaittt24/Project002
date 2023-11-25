print("Welcome To Cherrywood Lounge")

while True:
    print("\nOptions")
    
    print("1.Book a Room")
    print("2.Checkout")
    print("3.Exit")

    options=input("Enter your Choice(1-3): ")

    if options =="1":
        room_number=int(input("Enter the room number you want to book: "))
        print("You have successfully booked room number "+ str(room_number))
       
     

    elif options=="2":
        
        
        print("you are checking out from room number "+str(room_number)+"?")
        print("Please pay us $500")
        pay=input("yes/no: ")

        if pay=="yes":
            print("We hope you had a pleasant stay!")


        elif pay=="no":
            while True=="stop":
                break
              
            print("Kindly pay your bill")
        for x in (pay):
                print(x)
        

    elif options=="3":
        print("Exiting Cherrywood Lounge")
        break
       
    else:
        print("ERROR")
