
def banking_system():
   
    password = input("Enter your password: ").strip()
    correct_password = "123"  

    if password != correct_password:
        raise ValueError("Incorrect password!")

    balance = 100000.0  
    print("\nWelcome to your secure banking system!\n")

    while True:
        option = input("Choose an option:\n"
                       "1. Check balance\n"
                       "2. Withdraw money\n"
                       "3. Exit\n").strip()

        if option == "1":
            print("\nYour current balance is:", balance)

        elif option == "2":
            while True:
                try:
                    amount = float(input("\nEnter withdrawal amount (less than 100000): "))
                    if amount > 0 and amount <= 100000:
                        if balance >= amount:
                            balance -=  amount
                            print("\nWithdrawal successful! New balance:", balance)
                            break
                        else:
                            print("\nInsufficient funds. Your balance is only", balance)
                    else:
                        raise ValueError("Invalid amount. Please enter a positive amount less than or equal to 100000.")
                except ValueError as e:
                    print("\nError:", e)

        elif option == "3":
            print("\nwelcome back gain!")
            break

        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    try:
        banking_system()
    except ValueError as e:
        print("\nProgram terminated due to error:", e)
