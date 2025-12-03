# finance_calculator.py

import math

print("Welcome to the Finance Calculator!")
print("Choose an option:")
print("1. Calculate interest on an investment")
print("2. Calculate monthly repayment on a home loan")

choice = input("Enter 1 or 2: ")

if choice == "1":
    # Investment calculator
    principal = float(input("Enter the amount you are investing (R): "))
    rate = float(input("Enter the annual interest rate (%): ")) / 100
    years = int(input("Enter the number of years you plan to invest: "))
    interest_type = input("Choose interest type - 'simple' or 'compound': ").lower()

    if interest_type == "simple":
        total = principal * (1 + rate * years)
    elif interest_type == "compound":
        total = principal * math.pow((1 + rate), years)
    else:
        print("Invalid interest type selected.")
        exit()

    print(f"\nYour investment will be worth R{total:.2f} after {years} years.")

elif choice == "2":
    # Home loan calculator
    loan_amount = float(input("Enter the loan amount (R): "))
    annual_rate = float(input("Enter the annual interest rate (%): ")) / 100
    months = int(input("Enter the number of months to repay the loan: "))

    monthly_rate = annual_rate / 12
    repayment = (monthly_rate * loan_amount) / (1 - math.pow((1 + monthly_rate), -months))

    print(f"\nYour monthly repayment will be R{repayment:.2f} over {months} months.")

else:
    print("Invalid selection. Please restart and choose 1 or 2.")
