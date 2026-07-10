print("=" * 50)
print("        SAFE CHAT APPLICATION")
print("        Developed By Mohit Gole")
print("=" * 50)

history= ""
totalmsg=0
totalwords=0
totalchar=0
badword=0



while True:

    print("========== MAIN MENU ==========")
    print("1. Start Chat")
    print("2. View Chat History")
    print("3. Search Word")
    print("4. Chat Statistics")
    print("5. About")
    print("6. Reset ")
    print("7. Exit")
    choice = int(input("\nEnter Your Choice : "))

    match choice:

        case 1:
            print("\nStart Chat Selected")

            user1=input("Enter User 1 Name : ")
            user2=input("Enter User 2 Name : ")

            user1exit=False
            user2exit=False
            warninguser1=0
            warninguser2=0

            while True :
                if user1exit==False:
                    orignalmsg1=input(user1 + " : ")
                    msg1=orignalmsg1.lower()
                    

                    if "stupid" in msg1:
                        msg1=msg1.replace("stupid","*******")
                        badword=badword+1
                        warninguser1=warninguser1+1
                        
                    if "idiot" in msg1:
                        msg1=msg1.replace("idiot","****")
                        badword=badword+1
                        warninguser1=warninguser1+1
                    if "fool" in msg1:
                        msg1=msg1.replace("fool","***")
                        badword=badword+1
                        warninguser1=warninguser1+1
                    
                    
   
                    if warninguser1 ==3 :
                        print("!!WARNING : Please use Respectfull Language ")

                    if warninguser1 >=5 :
                        print("!! User BLOCKED !! ")
                        user1exit=True
                    
                    print(user1 + " : "+msg1)

                    history=history + user1 + " : " +msg1 + "\n"

                    totalmsg=totalmsg+1
                    totalwords=totalwords+len(msg1.split())
                    totalchar=totalchar+len(msg1)

                    if msg1.lower()=="bye":
                        user1exit=True
                        print(user1 , "Left the Chat ")

                if user2exit==False:

                    orignalmsg2=input(user2 + " : ")
                    msg2=orignalmsg2.lower()
                    


                    if "stupid" in msg2:
                        msg2=msg2.replace("stupid","*******")
                        badword=badword+1
                        warninguser2=warninguser2+1
                        
                    if "idiot" in msg2:
                        msg2=msg2.replace("idiot","****")
                        badword=badword+1
                        warninguser2=warninguser2+1
                    if "fool" in msg2:
                        msg2=msg2.replace("fool","***")
                        badword=badword+1
                        warninguser2=warninguser2+1
                    
                    
                    
                    if warninguser2 ==3 :
                        print("!!WARNING : Please use Respectfull Language ")

                    if warninguser2 >=5 :
                        print("!! User BLOCKED !! ")
                        user2exit=True

                    print(user2 + " : "+msg2)
             
                    history=history + user2 + " : " +msg2 + "\n"
                    totalmsg=totalmsg+1
                    totalwords=totalwords+len(msg2.split())
                    totalchar=totalchar+len(msg2)


                    if msg2.lower()=="bye":
                        user2exit=True
                        print(user2 , "Left the Chat ")

                if user1exit==True and user2exit==True:
                    print("\n Both users Left the Chat ")
                    print("Chat Closed SuccessFully")
                    break

        case 2:
            print("\nView Chat History Selected")

            if history=="":
                print("\n No Chat History Available ")
            else:
                print("\n ===================== CHAT HISTORY ===============")
                print(history)



        case 3:
            print("\nSearch Word Selected")

            if history=="":
                print("\n No Chat History Available ")
            else:
                Word=input("Enter Word to search : ").lower()
                count=history.lower().count(Word)


                if count>0:
                     print("\nWord Found in Chat Histroy ")
                     print("\nTotal Occurances : ",count)
                else:
                     print("\nWord not FOUND  ")


        case 4:
            print("\nChat Statistics Selected")

            print("Total Messages : ",totalmsg)
            print("Total Words : ",totalwords)
            print("Total Character : ",totalchar)
            print("Bad Words Used : ",badword)

            if badword==0:
                print("Chat Rating : Excellent ")
            elif badword<=2:
                print("Chat Rating : Good ")
            elif badword<=4:
                print("Chat Rating : Average ")
            else:
                print("Chat Rating : Poor ")

       
        case 5:

            print("\n" + "=" * 50)
            print("        ABOUT SAFE CHAT APPLICATION")
            print("=" * 50)

            print("Project Name      : Safe Chat")
            print("Trained By        : Ajay Sir ")
            print("Developer         : Mohit Gole")
            print("Language          : Python")
            print("Project Type      : Console Based Chat Application")

            print("\nFeatures :")
            print("- Two User Chat")
            print("- Chat Ends When Both Users Type 'bye'")
            print("- Bad Word Filter")
            print("- Warning & User Block System")
            print("- Chat History")
            print("- Search Word in History")
            print("- Chat Statistics")
            print("- Chat Rating")
            print("- Reset Chat")

            print("\nThank You For Using Safe Chat ")
            print("=" * 50)

        case 6:
            history=""
            totalwords=0
            totalchar=0
            totalmsg=0
            badword=0
            
            print("\n All CHat History and Statistics Reset SuccessFully............")
        case 7:
            print("\nThank You For Using Safe Chat.")
            break

        case _:
            print("\nInvalid Choice!")