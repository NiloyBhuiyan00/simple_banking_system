def bank():
    accounts = {}  # Store accounts in a dictionary
    
    print("Select an operation:")
    print("2402. Finding account number")
    
    account_id = input("Enter account number: ")

    # Check if account exists
    if account_id == "2402":
        balance = 1000
        print(f"Current balance is {balance}")

        while True:
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter a choice (2/3/4): ")

            if choice == "2":
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print(f"Deposited {amount}, new balance is {balance}")
                else:
                    print("Enter a positive value")

            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                if 0 < amount <= balance:
                    balance -= amount
                    print(f"Withdrawn {amount}, new balance is {balance}")
                else:
                    print("Insufficient balance or invalid amount")

            elif choice == "4":
                print("Exiting...")
                break

            else:
                print("Enter a valid choice")

    else:
        # Create account option
        response = input("Create account? (yes/no): ").lower()
        if response == "yes":
            username = input("Enter a username: ")
            new_account_number = input("Enter a unique account number: ")

            # Check if account number already exists
            if new_account_number in accounts:
                print("Account number already exists. Try again.")
            else:
                password = input("Enter a password: ")
                accounts[new_account_number] = {
                    "username": username,
                    "password": password,
                    "balance": 0
                }
                print("Account created successfully!")
                print(f"Your account name is {username}, account number is {new_account_number}")

        else:
            print("Exiting...")

# Run the bank function
bank()
