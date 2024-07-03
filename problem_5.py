# Function to read account data from the file and return it as a dictionary
def read_accounts():
    accounts = {}
    try:
        with open('accounts.txt', 'r') as file:
            for line in file:
                account_number, balance = line.strip().split(',')
                accounts[account_number] = float(balance)
    except FileNotFoundError:
        pass
    return accounts

# Function to write account data to the file
def write_accounts(accounts):
    with open('accounts.txt', 'w') as file:
        for account_number, balance in accounts.items():
            file.write(f'{account_number},{balance}\n')

# Function to get the current balance for a given account number
def get_balance(account_number):
    accounts = read_accounts()
    if account_number in accounts:
        return accounts[account_number]
    else:
        raise ValueError(f"Account number {account_number} not found.")

# Function to update the balance for a given account number
def update_account(account_number, balance):
    accounts = read_accounts()
    accounts[account_number] = balance
    write_accounts(accounts)

# Function to deposit the specified amount into the given account number
def deposit(account_number, amount):
    if amount < 0:
        raise ValueError("Deposit amount must be positive.")
    
    accounts = read_accounts()
    if account_number in accounts:
        accounts[account_number] += amount
        write_accounts(accounts)
    else:
        raise ValueError(f"Account number {account_number} not found.")

# Function to withdraw the specified amount from the given account number
def withdraw(account_number, amount):
    if amount < 0:
        raise ValueError("Withdrawal amount must be positive.")
    
    accounts = read_accounts()
    if account_number in accounts:
        if accounts[account_number] >= amount:
            accounts[account_number] -= amount
            write_accounts(accounts)
        else:
            raise ValueError("Insufficient funds.")
    else:
        raise ValueError(f"Account number {account_number} not found.")

# Testing the functions
def main():
    # Display initial balances
    try:
        print("Initial Balances:")
        print(f"Account 1234567890: ${get_balance('1234567890'):.2f}")
        print(f"Account 0987654321: ${get_balance('0987654321'):.2f}")
    except ValueError as e:
        print(e)
    
    # Test deposit
    try:
        print("\nDepositing $500 to account 1234567890")
        deposit("1234567890", 500.0)
        print(f"New Balance: ${get_balance('1234567890'):.2f}")
    except ValueError as e:
        print(e)
    
    # Test withdrawal
    try:
        print("\nWithdrawing $200 from account 0987654321")
        withdraw("0987654321", 200.0)
        print(f"New Balance: ${get_balance('0987654321'):.2f}")
    except ValueError as e:
        print(e)
    
    # Test withdrawal with insufficient funds
    try:
        print("\nTrying to withdraw $2000 from account 1234567890 (should fail due to insufficient funds)")
        withdraw("1234567890", 2000.0)
    except ValueError as e:
        print(e)
    
    # Test non-existent account
    try:
        print("\nChecking balance for a non-existent account (should raise an error)")
        print(f"Balance: ${get_balance('0000000000'):.2f}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()