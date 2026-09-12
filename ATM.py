#Creating the list and variables
initial_am= 1000
cor_pin= 3807
print("---------ATM Management System-----------")
# Allow the user 3 attempts to enter the correct PIN
for attempt in range(3):
    pin = int(input("Enter Your PIN: "))

    if pin == cor_pin:
        print("\nLogin Successful!")
        break
    else:
        if attempt == 0:
            print("You have 2 attempts remaining.")
        elif attempt == 1:
            print("You have 1 attempt remaining.")
        elif attempt == 2:
            print("\nToo many incorrect attempts!")
            print("ATM is locked. Please try again later.")
            exit()
                       
while True:
        print("\n----ATM MENU----")
        print("1. Check Balance") 
        print("2. Deposit Amount") 
        print("3. Withdraw Amount") 
        print("4. Transaction History") 
        print("5. Logout") 
        
        choice=int(input("Enter Your Choice: "))
        
        if choice == 1:
            print("Your balance is: ",initial_am)
        
        elif choice == 2:
            amount1=float(input("Enter the amount to deposit: "))
            
            if amount1> 0:
                balance=amount1+initial_am
                print("Amount deposited successfully.")
                print("Updated balance:", balance)
            else:
                print("Invalid Amount")
            
        elif choice == 3:
            amount2=float(input("Enter the amount to be credited: "))
            
            if amount2>balance:
                print("Insufficient Balance")
            else:
                balance-=amount2
                print("Amount Witdrawn Successfully!")
                print("Updated Balance", balance)
                
        elif choice == 4:
         print("--Transaction History---------")
         print("Initial balance:",initial_am)
         print("Amount deposited",amount1)
         print("Amount Witdrawn", amount2)
         print("Updated Balance:",balance )
         print("Thanhk You")
        
        elif choice == 5:
            print("Thank you for working with our bank")
            break
            
        else:
            print("Invalid Choice")
          
else:
    print("Invalide PIN")
            
                                   