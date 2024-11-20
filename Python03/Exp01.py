# ATM Operation

def atm_withdrawal(amount):
    if amount % 100 != 0:
        print("Invalid amount. Please enter an amount that is a multiple of 100.")
        return
    
    notes = [2000, 500, 200, 100]  # Available denominations
    result = []
    
    for note in notes:
        count = amount // note  # Calculate the number of notes for the current denomination
        if count > 0:
            result.append(f"{count} note{'s' if count > 1 else ''} of {note} rupee{'s' if count > 1 else ''}")
            amount %= note  # Update the remaining amount
    
    # Display the result
    if result:
        print("Please take", ", ".join(result))

# Input: Enter the amount to withdraw
try:
    withdrawal_amount = int(input("Enter the amount to withdraw: "))
    atm_withdrawal(withdrawal_amount)
except ValueError:
    print("Invalid input. Please enter a numeric amount.")
