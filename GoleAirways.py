print("***********************")
print("     GOLE AIRWAYS      ")
print("***********************")

pnr=1001
book=False
nm=""
ag=0
fl=""
fr=""
to=""
st=""
amt=0
tot=50
bk=0

while True:

    print("\n1.View Flights")
    print("2.Book Ticket")
    print("3.Cancel Ticket")
    print("4.Boarding Pass")
    print("5.Booking Status")
    print("6.Seat Availability")
    print("7.Exit")

    ch=int(input("Enter choice: "))

    match ch:

        case 1:
            print("\nFlight No   Route                 Fare")
            print("GA101       Indore-Delhi          4500")
            print("GA102       Indore-Mumbai         3500")
            print("GA103       Indore-Bangalore      6000")

        case 2:
            if book:
                print("Ticket already booked")
            else:
                nm=input("Name : ")
                ag=int(input("Age : "))
                print("\n1.GA101 Delhi")
                print("2.GA102 Mumbai")
                print("3.GA103 Bangalore")
                f=int(input("Select : "))

                if f==1:
                    fl="GA101"
                    fr="Indore"
                    to="Delhi"
                    amt=4500
                elif f==2:
                    fl="GA102"
                    fr="Indore"
                    to="Mumbai"
                    amt=3500
                elif f==3:
                    fl="GA103"
                    fr="Indore"
                    to="Bangalore"
                    amt=6000
                else:
                    print("Wrong choice")
                    continue

                n=int(input("Tickets : "))
                amt=amt*n
                st="A"+str(pnr-1000)
                book=True
                bk=n

                print("\nTicket Booked")
                print("PNR :",pnr)
                print("Seat :",st)
                print("Total :",amt)

        case 3:
            if book:
                p=int(input("Enter PNR : "))
                if p==pnr:
                    print("Ticket Cancelled")
                    book=False
                    nm=""
                    ag=0
                    fl=""
                    fr=""
                    to=""
                    st=""
                    amt=0
                    bk=0
                else:
                    print("Invalid PNR")
            else:
                print("No booking found")

        case 4:
            if book:
                print("\n******** BOARDING PASS ********")
                print("Name   :",nm)
                print("Age    :",ag)
                print("PNR    :",pnr)
                print("Flight :",fl)
                print("From   :",fr)
                print("To     :",to)
                print("Seat   :",st)
                print("Status : Confirm")
                print("*******************************")
            else:
                print("Book ticket first")

        case 5:
            if book:
                print("\nBooking Status")
                print("Name :",nm)
                print("Flight :",fl)
                print("Tickets :",bk)
                print("Fare :",amt)
                print("Status : Confirm")
            else:
                print("No booking found")

        case 6:
            print("\nSeat Availability")
            print("Total Seats :",tot)
            if book:
                print("Booked Seats :",bk)
                print("Available :",tot-bk)
            else:
                print("Booked Seats : 0")
                print("Available :",tot)

        case 7:
            print("Thank You For Choosing GOLE AIRWAYS")
            break

        case _:
            print("Invalid Choice")