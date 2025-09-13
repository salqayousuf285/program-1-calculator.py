def update_balance(current_balance,deposit_amount):
    new_balance=current_balance + deposit_amount
    print("Your new total balance is:", new_balance)
current=int(input("Enter your current_balance: "))
deposit=int(input("Enter the deposit_amount: "))
update_balance(current,deposit)