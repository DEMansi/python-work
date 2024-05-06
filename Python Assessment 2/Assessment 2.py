def display_menu():

    print("Welcome To Tops Quiz Gaming Challange")
    print("-------------------------------------------------------------\n")
    print("\nSelect Your Role : ")

    print("\n1.Quiz Master")
    print("\n2.Quiz Craker")
    role=int(input("\nEnter Your Role : "))
    if role==1:
        print("\nWelcome Master")
        print("\nShake Your Brain And Add Some Challanging Questions...")
        print("-------------------------------------------------------------\n")
        d1={}
        while True:
            print("*****Display Menu****")
            print("\n1.Add Questions")
            print("\n2.View Questions")
            print("\n3.Delete Questions")
            print("\n4.Exit")
            
            choice=int(input("Which Operation You Want To Perform : "))
            if choice==1:

                #Add Question
                
                 question = input("Enter the question: ")         
                 option_a = input("Enter option A: ")
                 option_b = input("Enter option B: ")
                 answer=input("Enter Correct Answer : ")
                 d1[question]={"A":option_a,"B":option_b,"answer":answer}
                 print("Question Add Successfully!!!")

            elif choice==2:

                #view Question

                if len(d1) > 0:
                    for key,value in d1.items():
                        print(key, " : ", value)
                else:
                    print("No questions available to view.")

            elif choice==3:
                #Delete Questions
                if len(d1) > 0:
                    key = input("Enter the question to delete: ")
                    if key in d1:
                        d1.pop(key)
                        print("Question deleted successfully!")
                    else:
                        print("Question not found!")
                else:
                    print("No questions available to delete.")

            elif choice==4:
                #Exit
                print("Thank you!!!!")
                break

display_menu()
