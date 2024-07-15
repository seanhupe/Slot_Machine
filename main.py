def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

    return amount


deposit()


# Collect the bet from the user, and how many lines.  (bet * lines)
def get_number_of_lines():




def main():
    balance = deposit()


main()

